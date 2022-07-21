from _typeshed import Incomplete
from collections.abc import Generator

def graph_edit_distance(
    G1,
    G2,
    node_match: Incomplete | None = ...,
    edge_match: Incomplete | None = ...,
    node_subst_cost: Incomplete | None = ...,
    node_del_cost: Incomplete | None = ...,
    node_ins_cost: Incomplete | None = ...,
    edge_subst_cost: Incomplete | None = ...,
    edge_del_cost: Incomplete | None = ...,
    edge_ins_cost: Incomplete | None = ...,
    roots: Incomplete | None = ...,
    upper_bound: Incomplete | None = ...,
    timeout: Incomplete | None = ...,
): ...
def optimal_edit_paths(
    G1,
    G2,
    node_match: Incomplete | None = ...,
    edge_match: Incomplete | None = ...,
    node_subst_cost: Incomplete | None = ...,
    node_del_cost: Incomplete | None = ...,
    node_ins_cost: Incomplete | None = ...,
    edge_subst_cost: Incomplete | None = ...,
    edge_del_cost: Incomplete | None = ...,
    edge_ins_cost: Incomplete | None = ...,
    upper_bound: Incomplete | None = ...,
): ...
def optimize_graph_edit_distance(
    G1,
    G2,
    node_match: Incomplete | None = ...,
    edge_match: Incomplete | None = ...,
    node_subst_cost: Incomplete | None = ...,
    node_del_cost: Incomplete | None = ...,
    node_ins_cost: Incomplete | None = ...,
    edge_subst_cost: Incomplete | None = ...,
    edge_del_cost: Incomplete | None = ...,
    edge_ins_cost: Incomplete | None = ...,
    upper_bound: Incomplete | None = ...,
) -> Generator[Incomplete, None, None]: ...
def optimize_edit_paths(
    G1,
    G2,
    node_match: Incomplete | None = ...,
    edge_match: Incomplete | None = ...,
    node_subst_cost: Incomplete | None = ...,
    node_del_cost: Incomplete | None = ...,
    node_ins_cost: Incomplete | None = ...,
    edge_subst_cost: Incomplete | None = ...,
    edge_del_cost: Incomplete | None = ...,
    edge_ins_cost: Incomplete | None = ...,
    upper_bound: Incomplete | None = ...,
    strictly_decreasing: bool = ...,
    roots: Incomplete | None = ...,
    timeout: Incomplete | None = ...,
) -> Generator[Incomplete, None, Incomplete]: ...
def simrank_similarity(
    G,
    source: Incomplete | None = ...,
    target: Incomplete | None = ...,
    importance_factor: float = ...,
    max_iterations: int = ...,
    tolerance: float = ...,
): ...
def _simrank_similarity(
    G,
    source: Incomplete | None = ...,
    target: Incomplete | None = ...,
    importance_factor: float = ...,
    max_iterations: int = ...,
    tolerance: float = ...,
): ...
def _simrank_similarity_python(
    G,
    source: Incomplete | None = ...,
    target: Incomplete | None = ...,
    importance_factor: float = ...,
    max_iterations: int = ...,
    tolerance: float = ...,
): ...
def panther_similarity(
    G,
    source,
    k: int = ...,
    path_length: int = ...,
    c: float = ...,
    delta: float = ...,
    eps: Incomplete | None = ...,
): ...
def generate_random_paths(
    G, sample_size, path_length: int = ..., index_map: Incomplete | None = ...
) -> Generator[Incomplete, None, None]: ...
