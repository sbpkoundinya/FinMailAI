# Financial Email Classifier with OCR & ServiceNow Integration

![System Architecture](docs/architecture.png)

## Features
- 📧 Process .eml files with/without attachments
- 🔍 OCR for PDFs, images (PNG/JPG), and Office docs
- 🏷️ AI classification (11 categories, 32 subcategories)
- 🎫 Automatic ServiceNow ticket creation
- 📊 Confidence scoring with explainability

## Quick Start

```bash
# Clone repository
git clone https://github.com/yourrepo/financial-email-classifier.git
cd financial-email-classifier

# Install dependencies
pip install -r requirements.txt

# Run service (dev mode)
uvicorn src.app.main:app --reload