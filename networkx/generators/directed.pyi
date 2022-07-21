from _typeshed import Incomplete

def gn_graph(
    n,
    kernel: Incomplete | None = ...,
    create_using: Incomplete | None = ...,
    seed: Incomplete | None = ...,
): ...
def gnr_graph(
    n, p, create_using: Incomplete | None = ..., seed: Incomplete | None = ...
): ...
def gnc_graph(
    n, create_using: Incomplete | None = ..., seed: Incomplete | None = ...
): ...
def scale_free_graph(
    n,
    alpha: float = ...,
    beta: float = ...,
    gamma: float = ...,
    delta_in: float = ...,
    delta_out: int = ...,
    create_using: Incomplete | None = ...,
    seed: Incomplete | None = ...,
    initial_graph: Incomplete | None = ...,
): ...
def random_k_out_graph(
    n, k, alpha, self_loops: bool = ..., seed: Incomplete | None = ...
): ...
