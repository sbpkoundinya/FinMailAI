# Service layer exports
from .email_parser import parse_eml
from .classifier import classify_email
from .servicenow import create_ticket
from .attachment_processor import AttachmentProcessor

processor = AttachmentProcessor()

__all__ = [
    "parse_eml",
    "classify_email",
    "create_ticket",
    "processor.process_attachment"
]