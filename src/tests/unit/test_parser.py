import pytest
from src.app.services.email_parser import parse_eml

def test_multipart_parsing():
    with open("tests/emls/multipart.eml", "rb") as f:
        result = parse_eml(f.read())
        assert len(result["attachments"]) == 2
        assert "Final Invoice" in result["body"]