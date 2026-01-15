from pydantic import BaseModel
from typing import List, Optional

class CodeSubmission(BaseModel):
    filename: str
    code: str

class VulnerabilitySchema(BaseModel):
    severity: str
    vuln_type: str
    description: str
    suggested_patch: str

    class Config:
        from_attributes = True

class ScanResponse(BaseModel):
    id: int
    filename: str
    code_content: str
    vulnerabilities: List[VulnerabilitySchema]

    class Config:
        from_attributes = True