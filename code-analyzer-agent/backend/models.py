from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Scan(Base):
    __tablename__ = "scans"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    code_content = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    vulnerabilities = relationship("Vulnerability", back_populates="scan")

class Vulnerability(Base):
    __tablename__ = "vulnerabilities"
    id = Column(Integer, primary_key=True, index=True)
    scan_id = Column(Integer, ForeignKey("scans.id"))
    severity = Column(String)
    vuln_type = Column(String)
    description = Column(Text)
    suggested_patch = Column(Text)
    scan = relationship("Scan", back_populates="vulnerabilities")