from _typeshed import Incomplete

def geometric_edges(G, radius, p: int = ...): ...
def random_geometric_graph(
    n,
    radius,
    dim: int = ...,
    pos: Incomplete | None = ...,
    p: int = ...,
    seed: Incomplete | None = ...,
): ...
def soft_random_geometric_graph(
    n,
    radius,
    dim: int = ...,
    pos: Incomplete | None = ...,
    p: int = ...,
    p_dist: Incomplete | None = ...,
    seed: Incomplete | None = ...,
): ...
def geographical_threshold_graph(
    n,
    theta,
    dim: int = ...,
    pos: Incomplete | None = ...,
    weight: Incomplete | None = ...,
    metric: Incomplete | None = ...,
    p_dist: Incomplete | None = ...,
    seed: Incomplete | None = ...,
): ...
def waxman_graph(
    n,
    beta: float = ...,
    alpha: float = ...,
    L: Incomplete | None = ...,
    domain=...,
    metric: Incomplete | None = ...,
    seed: Incomplete | None = ...,
): ...
def navigable_small_world_graph(
    n,
    p: int = ...,
    q: int = ...,
    r: int = ...,
    dim: int = ...,
    seed: Incomplete | None = ...,
): ...
def thresholded_random_geometric_graph(
    n,
    radius,
    theta,
    dim: int = ...,
    pos: Incomplete | None = ...,
    weight: Incomplete | None = ...,
    p: int = ...,
    seed: Incomplete | None = ...,
): ...
