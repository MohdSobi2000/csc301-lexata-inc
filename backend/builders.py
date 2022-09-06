from .risk_factor import RiskFactor
from .company import Company
from .filing import Filing


# ===== risk factors methods =====

def build_rf(json_dict: dict) -> RiskFactor | None:
    rf = RiskFactor()
    try:
        rf.set_text(json_dict["text"])
        rf.set_embeddings(json_dict["embeddings"])
        rf.set_header(json_dict["header"])
    except KeyError:
        return None
    return rf

# ===== companies methods =====

def build_c(json_dict: dict) -> Company | None:
    c = Company()
    try:
        c.set_ticker(json_dict["ticker"])
        c.set_company_name(json_dict["company_name"])
        c.set_sector(json_dict["sector"])
        c.set_jurisdiction(json_dict["jurisdiction"])
        if "num_filings" in json_dict:
            c.set_num_filings(json_dict["num_filings"])
    except KeyError:
        return None
    return c

# ===== filings methods ======

def build_f(json_dict: dict) -> Filing | None:
    f = Filing()
    try:
        f.set_date(json_dict["date_of_filing"])
        f.set_link(json_dict["link_to_filing"])
        f.set_filing_id(json_dict["filing_id"])
    except KeyError:
        return None
    return f