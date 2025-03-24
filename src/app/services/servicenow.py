import requests
from ..config import settings
from ..schemas import ClassificationResult
from typing import Dict, Any

PRIORITY_MAP = {
    "high": "1",
    "medium": "2", 
    "low": "3"
}

async def create_ticket(email: Dict[str, Any], classification: ClassificationResult) -> Dict[str, Any]:
    payload = {
        "short_description": f"{classification.category.upper()}: {email['subject']}",
        "description": email["body"][:4000],
        "urgency": PRIORITY_MAP.get(classification.priority, "3"),
        "assignment_group": get_assignment_group(classification),
        "comments": format_comments(classification)
    }
    
    response = requests.post(
        f"{settings.snow_instance}/api/now/table/incident",
        auth=(settings.snow_username, settings.snow_password),
        json=payload,
        timeout=10
    )
    response.raise_for_status()
    return response.json()

def get_assignment_group(classification: ClassificationResult) -> str:
    mapping = {
        "money_movement": "Payments",
        "bank_guarantee": "Trade Finance",
        "trade_finance": "Trade Operations"
    }
    return mapping.get(classification.category.split('_')[0], "Finance")

def format_comments(classification: ClassificationResult) -> str:
    return f"""Auto-classified as {classification.category} ({classification.confidence:.0%} confidence)
Entities detected: {', '.join(f"{k}: {len(v)}" for k,v in classification.entities.items())}"""