from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .services.email_parser import parse_eml
from .services.classifier import classify_email
from .services.servicenow import create_ticket
from .schemas import ProcessedEmail
import logging

app = FastAPI(title="Financial Email Classifier")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process", response_model=ProcessedEmail)
async def process_email(file: UploadFile):
    try:
        # 1. Parse email
        eml_content = await file.read()
        parsed = await parse_eml(eml_content)
        
        # 2. Classify content
        classification = await classify_email(
            parsed["body"],
            [att["content"] for att in parsed["attachments"]]
        )
        
        # 3. Create ServiceNow ticket
        ticket = await create_ticket(parsed, classification)
        
        return {
            **parsed,
            "classification": classification,
            "ticket_id": ticket["sys_id"]
        }
        
    except Exception as e:
        logging.error(f"Processing failed: {str(e)}")
        raise HTTPException(500, detail="Email processing error")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}