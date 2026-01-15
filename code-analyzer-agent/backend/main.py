from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import models, scanner, schemas
from fastapi.middleware.cors import CORSMiddleware
import json

Base.metadata.create_all(bind=engine) # Creates tables in Supabase
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/scan")
def run_new_scan(submission: schemas.CodeSubmission, db: Session = Depends(get_db)):
    # 1. Save scan entry
    new_scan = models.Scan(filename=submission.filename, code_content=submission.code)
    db.add(new_scan)
    db.commit()
    db.refresh(new_scan)
    
    # 2. Run AI Analysis
    analysis_result = scanner.analyze_code(submission.code)
    
    # 3. Save vulnerabilities found by LLM
    for v in analysis_result.get('vulnerabilities', []):
        vuln = models.Vulnerability(
            scan_id=new_scan.id,
            severity=v['severity'],
            vuln_type=v['type'],
            description=v['description'],
            suggested_patch=v['patch']
        )
        db.add(vuln)
    
    db.commit()
    return {"scan_id": new_scan.id}

@app.get("/scans/{scan_id}", response_model=schemas.ScanResponse)
def get_scan_details(scan_id: int, db: Session = Depends(get_db)):
    scan = db.query(models.Scan).filter(models.Scan.id == scan_id).first()
    if not scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    return scan