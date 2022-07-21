from _typeshed import Incomplete
from networkx.algorithms.flow import edmonds_karp

default_flow_func = edmonds_karp

def local_node_connectivity(
    G,
    s,
    t,
    flow_func: Incomplete | None = ...,
    auxiliary: Incomplete | None = ...,
    residual: Incomplete | None = ...,
    cutoff: Incomplete | None = ...,
): ...
def node_connectivity(
    G,
    s: Incomplete | None = ...,
    t: Incomplete | None = ...,
    flow_func: Incomplete | None = ...,
): ...
def average_node_connectivity(G, flow_func: Incomplete | None = ...): ...
def all_pairs_node_connectivity(
    G, nbunch: Incomplete | None = ..., flow_func: Incomplete | None = ...
): ...
def local_edge_connectivity(
    G,
    s,
    t,
    flow_func: Incomplete | None = ...,
    auxiliary: Incomplete | None = ...,
    residual: Incomplete | None = ...,
    cutoff: Incomplete | None = ...,
): ...
def edge_connectivity(
    G,
    s: Incomplete | None = ...,
    t: Incomplete | None = ...,
    flow_func: Incomplete | None = ...,
    cutoff: Incomplete | None = ...,
): ...
