from src.app.services.edgecase_handlers.legal_docs import LegalDocParser

@pytest.fixture
def legal_parser():
    return LegalDocParser()

def test_legal_clause_extraction(legal_parser):
    with open("tests/edge_cases/contract.pdf", "rb") as f:
        result = legal_parser.extract_clauses(f.read())
        assert "governing_law" in result["page_0"]