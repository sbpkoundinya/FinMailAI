from pydantic import BaseModel
from typing import Optional, List, Dict

class EmailAttachment(BaseModel):
    filename: str
    content_type: str
    size: int
    extracted_text: Optional[str] = None

class ClassificationResult(BaseModel):
    is_request: bool
    category: str
    subcategory: Optional[str]
    confidence: float
    entities: Dict[str, List[str]]
    priority: str = "medium"

class ProcessedEmail(BaseModel):
    subject: str
    sender: str
    body: str
    attachments: List[EmailAttachment]
    classification: ClassificationResult