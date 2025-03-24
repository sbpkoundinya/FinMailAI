import openai
import json
from ..config import settings
from ..schemas import ClassificationResult
from typing import List

PROMPT_TEMPLATE = """
Analyze this financial email and attachments. Classify as:

Categories: 
- money_movement_inbound (subtypes: principal, interest, fees)
- money_movement_outbound (subtypes: payment, transfer)
- bank_guarantee (subtypes: issuance, amendment)
- trade_finance (subtypes: lc, collections)

Output JSON format:
{{
    "is_request": bool,
    "category": str,
    "subcategory": str|null,
    "priority": "low|medium|high",
    "entities": {{
        "amounts": list,
        "dates": list,
        "accounts": list
    }}
}}

Content:
{content}
"""

async def classify_email(body: str, attachments: List[bytes]) -> ClassificationResult:
    combined_text = body + "\n\n" + "\n\n".join(
        extract_text_from_attachment(att) for att in attachments
    )
    
    response = await openai.ChatCompletion.acreate(
        model=settings.openai_model,
        messages=[{
            "role": "system",
            "content": PROMPT_TEMPLATE.format(content=combined_text)
        }],
        temperature=0.3,
        max_tokens=500
    )
    
    result = json.loads(response.choices[0].message.content)
    return ClassificationResult(**result)

def extract_text_from_attachment(content: bytes) -> str:
    # Simplified - would integrate Tesseract here
    return content.decode("utf-8", errors="ignore")[:5000]