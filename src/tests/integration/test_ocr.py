import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from app.services.attachment_processor import AttachmentProcessor

def test_pdf_ocr():
    with open("tests/attachments/contract.pdf", "rb") as f:
        processor = AttachmentProcessor()
        result = processor.process(f.read(), "application/pdf")
        assert "USD 1,000,000" in result["text"]