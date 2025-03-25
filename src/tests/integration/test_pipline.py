import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@pytest.fixture
def sample_eml():
    return """MIME-Version: 1.0
Subject: Test Payment
From: test@bank.com
Content-Type: text/plain

Payment of USD 1000"""

def test_full_pipeline(sample_eml):
    with patch('app.services.classifier.openai.ChatCompletion.acreate') as mock_openai:
        mock_openai.return_value = {
            "choices": [{"message": {"content": """{
                "is_request": false,
                "category": "money_movement_inbound",
                "entities": {"amounts": ["USD 1000"]}
            }"""}}]
        }
        
        response = client.post(
            "/process",
            files={"file": ("test.eml", sample_eml)},
            headers={"Authorization": "Bearer test"}
        )
        
        assert response.status_code == 200
        assert response.json()["classification"]["category"] == "money_movement_inbound"