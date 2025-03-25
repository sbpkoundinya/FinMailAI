import pytest
from src.app.services.classifier import FinancialClassifier

@pytest.mark.parametrize("text,expected", [
    ("支付 ¥1,000,000", {"currency": "CNY", "amount": 1000000}),
    ("دفع 1,000,000 ريال", {"currency": "SAR", "amount": 1000000})
])
def test_multilingual_amounts(text, expected):
    result = FinancialClassifier().extract_entities(text)
    assert result["amounts"][0] == expected["amount"]
    assert expected["currency"] in result["currencies"]