import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from app.services.classifier import classify_email
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_classify_money_movement():
    mock_openai = AsyncMock()
    mock_openai.ChatCompletion.acreate.return_value = {
        "choices": [{"message": {"content": """{
            "is_request": false,
            "category": "money_movement_inbound",
            "subcategory": "principal",
            "priority": "high",
            "entities": {
                "amounts": ["USD 1000"],
                "dates": ["2023-01-01"]
            }
        }"""}}]
    }
    
    result = await classify_email("Payment of USD 1000", [])
    assert result.category == "money_movement_inbound"
    assert result.priority == "high"