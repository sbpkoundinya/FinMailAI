def test_amendment_tracking():
    email = """
    ORIGINAL: USD 1,000,000
    AMENDED: USD 1,500,000
    """
    amounts = FinancialClassifier().extract_entities(email)["amounts"]
    assert sorted(amounts) == [1000000, 1500000]