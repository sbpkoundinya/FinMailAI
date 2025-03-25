# Financial Email Classifier with OCR & ServiceNow Integration
<img width="825" alt="image" src="https://github.com/user-attachments/assets/c59dfd17-794c-4d51-a6b3-d03ac8688c8a" />

## Model Summary

An AI-powered pipeline that:
1. Ingests .eml files with attachments
2. Classifies financial requests using GPT-4 with finetuned adapters
3. Processes documents with hybrid OCR (Tesseract + LayoutLMv3)
4. Automates ServiceNow ticketing with SLA-based routing

## Key Features
-> Email Classification: Categorizes emails into request and sub-request types.
-> Field Extraction: Extracts key financial data from email body and attachments.
-> Duplicate Detection: Identifies and flags duplicate emails.
-> Confidence Scoring: Provides a confidence score for each classification.
-> Dynamic Priority Source Handling: Determines whether to extract data from the email body, attachment, or both.

## Tech Stack
<img width="425" alt="image" src="https://github.com/user-attachments/assets/a7ac7390-9c76-4858-a0fd-6f3bf555957d" />

## Dependencies
Python 3.10+
pip
virtualenv
OpenAI API key (for classification logic)

## Docker Deployment

```bash
docker-compose up -d --build

# Verify
curl http://localhost:8000/health
```

## ServiceNow Integration
## Configuration

```ini
# .env
OPENAI_API_KEY=your_api_key
SNOW_INSTANCE=dummy_instance
SNOW_USERNAME=dummy_username
SNOW_PASSWORD=dummy_password

## Ticket Mapping
<img width="346" alt="image" src="https://github.com/user-attachments/assets/4c37195a-4f2f-4b8a-b0ef-b72f15244cb0" />
```

## Test Strategy

```
        [E2E] 10%
       /         \
   [Integration]  20%
      /             \
[Unit Tests]        70%
```

## Logging Strategy

```bash
# src/app/config.py
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('finmailai.log'),
        logging.StreamHandler()
    ]
)

# Install dependencies
pip install -r requirements.txt

# Run service (dev mode)
uvicorn src.app.main:app --reload
```

## Log Samples

```bash
2023-11-21 14:30:45 [INFO] Processed email from invoices@acme.com
2023-11-21 14:31:02 [WARNING] Low OCR confidence (62%) on attachment contract.pdf
2023-11-21 14:31:15 [ERROR] ServiceNow API timeout (URL: /api/now/table/incident)
```

## Troubleshooting

```bash
# Check OCR issues
tesseract --list-langs

# Debug API calls
curl -v http://localhost:8000/process -F file=@test.eml

# View logs
docker-compose logs -f
```
