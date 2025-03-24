import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
import io
import re
from typing import Dict, Any

class AttachmentProcessor:
    FINANCIAL_PATTERNS = {
        "amount": r"\b(?:USD|EUR|GBP)\s?\d{1,3}(?:,\d{3})*\.\d{2}\b",
        "date": r"\b\d{2}[-\/]\d{2}[-\/]\d{4}\b",
        "account": r"\b[A-Z]{2}\d{2}[\s-]?[A-Z0-9]{4}[\s-]?\d{7}\b",
        "swift": r"\b[A-Z]{6}[A-Z0-9]{2}(?:[A-Z0-9]{3})?\b"
    }

    async def process(self, content: bytes, content_type: str) -> Dict[str, Any]:
        """Process attachment content based on type"""
        try:
            if content_type == "application/pdf":
                return await self._process_pdf(content)
            elif content_type.startswith("image/"):
                return await self._process_image(content)
            else:
                return self._extract_entities(content.decode("utf-8", errors="ignore"))
        except Exception as e:
            return {"error": str(e), "text": ""}

    async def _process_pdf(self, content: bytes) -> Dict[str, Any]:
        images = convert_from_bytes(content)
        full_text = ""
        for img in images:
            text = pytesseract.image_to_string(img)
            full_text += text + "\n"
        return self._extract_entities(full_text)

    async def _process_image(self, content: bytes) -> Dict[str, Any]:
        img = Image.open(io.BytesIO(content))
        text = pytesseract.image_to_string(img)
        return self._extract_entities(text)

    def _extract_entities(self, text: str) -> Dict[str, Any]:
        entities = {}
        for entity_type, pattern in self.FINANCIAL_PATTERNS.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                entities[entity_type] = list(set(matches))  # Remove duplicates
        return {
            "text": text[:5000],  # Limit extracted text
            "entities": entities
        }

# Singleton instance
processor = AttachmentProcessor()