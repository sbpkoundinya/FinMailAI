import email
from email import policy
from io import BytesIO
from typing import Dict, Any

async def parse_eml(eml_content: bytes) -> Dict[str, Any]:
    msg = email.message_from_bytes(eml_content, policy=policy.default)
    
    result = {
        "subject": msg["subject"] or "",
        "sender": msg["from"],
        "body": "",
        "attachments": []
    }

    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            result["body"] = part.get_content()
        elif part.get_filename():
            result["attachments"].append({
                "filename": part.get_filename(),
                "content_type": part.get_content_type(),
                "content": part.get_payload(decode=True)
            })

    return result