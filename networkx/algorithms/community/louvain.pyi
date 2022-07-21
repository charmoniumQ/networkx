from collections.abc import Generator

from _typeshed import Incomplete

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
