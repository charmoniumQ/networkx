from _typeshed import Incomplete

class _PCGSolver:
    def __init__(self, A, M) -> None: ...
    def solve(self, B, tol): ...

class _LUSolver:
    def __init__(self, A) -> None: ...
    def solve(self, B, tol: Incomplete | None = ...): ...

def algebraic_connectivity(
    G,
    weight: str = ...,
    normalized: bool = ...,
    tol: float = ...,
    method: str = ...,
    seed: Incomplete | None = ...,
): ...
def fiedler_vector(
    G,
    weight: str = ...,
    normalized: bool = ...,
    tol: float = ...,
    method: str = ...,
    seed: Incomplete | None = ...,
): ...
def spectral_ordering(
    G,
    weight: str = ...,
    normalized: bool = ...,
    tol: float = ...,
    method: str = ...,
    seed: Incomplete | None = ...,
): ...
