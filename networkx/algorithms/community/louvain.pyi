from _typeshed import Incomplete
from collections.abc import Generator

def louvain_communities(
    G,
    weight: str = ...,
    resolution: int = ...,
    threshold: float = ...,
    seed: Incomplete | None = ...,
): ...
def louvain_partitions(
    G,
    weight: str = ...,
    resolution: int = ...,
    threshold: float = ...,
    seed: Incomplete | None = ...,
) -> Generator[Incomplete, None, None]: ...
