from _typeshed import Incomplete

def _extrema_bounding(G, compute: str = "diameter"): ...
def eccentricity(G, v: Incomplete | None = ..., sp: Incomplete | None = ...): ...
def diameter(G, e: Incomplete | None = ..., usebounds: bool = ...): ...
def periphery(G, e: Incomplete | None = ..., usebounds: bool = ...): ...
def radius(G, e: Incomplete | None = ..., usebounds: bool = ...): ...
def center(G, e: Incomplete | None = ..., usebounds: bool = ...): ...
def barycenter(
    G,
    weight: Incomplete | None = ...,
    attr: Incomplete | None = ...,
    sp: Incomplete | None = ...,
): ...
def resistance_distance(
    G, nodeA, nodeB, weight: Incomplete | None = ..., invert_weight: bool = ...
): ...
