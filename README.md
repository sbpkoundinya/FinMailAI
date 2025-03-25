# Financial Email Classifier with OCR & ServiceNow Integration

![System Architecture](docs/architecture.png)

## Model Summary

An AI-powered pipeline that:
1. Ingests .eml files with attachments
2. Classifies financial requests using GPT-4 with finetuned adapters
3. Processes documents with hybrid OCR (Tesseract + LayoutLMv3)
4. Automates ServiceNow ticketing with SLA-based routing

## Key Features
<img width="485" alt="image" src="https://github.com/user-attachments/assets/1c4599cd-5e15-4162-a55d-bc86ea7292a5" />

## Tech Stack
<img width="425" alt="image" src="https://github.com/user-attachments/assets/a7ac7390-9c76-4858-a0fd-6f3bf555957d" />

## Dependencies
fastapi==0.95.2
openai==0.27.8
pytesseract==0.3.10
pdf2image==1.16.3
transformers==4.30.0
requests==2.31.0
python-dotenv==1.0.0

## Prerequisites

```bash
# Ubuntu
sudo apt-get install tesseract-ocr poppler-utils libtesseract-dev

# MacOS
brew install tesseract poppler
```

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
SNOW_INSTANCE=https://your-instance.service-now.com
SNOW_USERNAME=api_user
SNOW_PASSWORD=your_password

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

