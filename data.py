from dataclasses import dataclass, astuple, asdict


@dataclass(frozen=True, order=True)
class EnsembleClass:
    geneID: int
    seqStartPos: int
    seqStopPos: int
    strand: int
    description: str

