# A class representing a Risk Factors in the Lexata database.
class RiskFactor:

    comparator = None

    def __init__(self):
        self.text = None
        self.embeddings = None
        self.header = None

    # ===== setter methods =====

    def set_text(self, text: str):
        self.text = text

    def set_embeddings(self, embeddings: list[int]):
        if len(embeddings) != 2048:
            raise ValueError("embeddings must have size 2048")
        self.embeddings = embeddings

    def set_header(self, header: str):
        self.header = header

    # ===== comparator =====

    def __lt__(self, other) -> bool:
        if self.comparator is None:
            raise NotImplementedError("comparator must be set to compare risk factors")
        return RiskFactor.comparator(self.embeddings, other.embeddings)

    # ===== serialization methods =====

    def to_dict(self) -> dict:
        return {
            "header": self.header,
            "text": self.text,
            "embeddings": self.embeddings
        }
