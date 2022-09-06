"""
A class which represents and models a Filing in the Lexata Database. Provides validation to certain fields, and a
method to serialize the information into a dictionary to easily by stored by MongoDB or to be returned via the module.

"""

import validators

from datetime import datetime

class Filing:

    def __init__(self):
        self.date_of_filing = None
        self.link_to_filing = None
        self.filing_id = None

    # ===== getter methods =====

    def get_filing_id(self) -> int:
        return self.filing_id

    # ===== setter methods =====

    def set_date(self, date: str):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            self.date_of_filing = date
        except Exception:
            raise ValueError("date must be of the format: YYYY-MM-DD")

    def set_link(self, link: str):
        if not validators.url(link):
            raise ValueError("link to filing must be a valid URL")
        self.link_to_filing = link

    def set_filing_id(self, filing_id: int):
        self.filing_id = filing_id

    # ===== serialization methods =====

    def to_dict(self) -> dict:
        return {
            "date_of_filing": self.date_of_filing,
            "link_to_filing": self.link_to_filing,
            "filing_id": self.filing_id
        }
