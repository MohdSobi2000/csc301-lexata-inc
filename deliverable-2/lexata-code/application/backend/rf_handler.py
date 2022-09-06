"""
A use case class for Risk Factors. Compiles together information from all three major components of the database - Risk
Factors, Filings, and Companies. Provides a method for compiling the information into a dictionary.

This class wraps the comparison of RiskFactors, overriding the __lt__() function to instead compare the risk factor
stored by this class. Also encapsulates the setting of the RiskFactor.comparator field.

"""

from typing import Callable, Any

from risk_factor import RiskFactor
from company import Company
from filing import Filing

class RiskFactorHandler:

    def __init__(self, rf: RiskFactor, f: Filing, c: Company):
        self.risk_factor = rf
        self.filing = f
        self.company = c

    def __lt__(self, other):
        return self.risk_factor < other.risk_factor

    def to_dict(self):
        return {
            "risk factor": self.risk_factor.to_dict(),
            "filing details": self.filing.to_dict(),
            "company details": self.company.to_dict()
        }

    @staticmethod
    def set_rf_comparator(comparator: Callable[[Any, Any], bool]) -> None:
        RiskFactor.comparator = comparator

    @staticmethod
    def unset_rf_comparator() -> None:
        RiskFactor.comparator = None