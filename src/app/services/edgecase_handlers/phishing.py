import re
from typing import Dict

class PhishingDetector:
    def __init__(self):
        self.rules = [
            (r"urgent\s+action\s+required", 0.9),
            (r"click\s+here\s+to\s+verify", 0.95)
        ]

    def analyze(self, email: Dict) -> float:
        confidence = 0.0
        text = f"{email['subject']} {email['body']}".lower()
        
        for pattern, score in self.rules:
            if re.search(pattern, text):
                confidence = max(confidence, score)
                
        return confidence