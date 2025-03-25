import pytesseract
from pdf2image import convert_from_bytes
from .edgecase_handlers.currency_normalizer import normalize_currency

class AttachmentProcessor:
    def process_attachment(self, content: bytes, content_type: str) -> dict:
        if content_type == "application/pdf":
            images = convert_from_bytes(content)
            text = " ".join(pytesseract.image_to_string(img) for img in images)
        else:
            text = pytesseract.image_to_string(content)
        
        return {
            "text": normalize_currency(text),
            "entities": self._extract_entities(text)
        }