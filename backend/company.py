# A class representing a Company in the Lexata database.
class Company:

    def __init__(self):
        self.ticker = None
        self.company_name = None
        self.sector = None
        self.jurisdiction = None
        self.num_filings = 0

    # ===== getter methods =====

    def get_ticker(self) -> str:
        return self.ticker

    def get_num_filings(self) -> int:
        return self.num_filings

    # ===== setter methods =====

    def set_ticker(self, ticker: str):
        self.ticker = ticker

    def set_company_name(self, name: str):
        self.company_name = name

    def set_sector(self, sector: str):
        self.sector = sector

    def set_jurisdiction(self, jurisdiction: str):
        self.jurisdiction = jurisdiction

    def set_num_filings(self, num_filings):
        self.num_filings = num_filings

    def add_filing(self):
        self.num_filings += 1

    # ===== serialization methods =====

    def to_dict(self):
        return {
            "ticker": self.ticker,
            "company_name": self.company_name,
            "sector": self.sector,
            "jurisdiction": self.jurisdiction,
            "num_filings": self.num_filings
        }
