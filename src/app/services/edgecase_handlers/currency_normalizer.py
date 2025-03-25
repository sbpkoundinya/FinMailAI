CURRENCY_MAP = {
    "¥": "CNY",
    "£": "GBP",
    "€": "EUR",
    "₽": "RUB",
    "₹": "INR"
}

def normalize_currency(text: str) -> str:
    for symbol, code in CURRENCY_MAP.items():
        text = re.sub(rf"{symbol}\s*(\d+)", f"{code} \1", text)
    return text