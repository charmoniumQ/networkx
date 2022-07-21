from _typeshed import Incomplete

from networkx.algorithms.flow import edmonds_karp

default_flow_func = edmonds_karp

def minimum_st_edge_cut(
    G,
    s,
    t,
    flow_func: Incomplete | None = ...,
    auxiliary: Incomplete | None = ...,
    residual: Incomplete | None = ...,
): ...
def minimum_st_node_cut(
    G,
    s,
    t,
    flow_func: Incomplete | None = ...,
    auxiliary: Incomplete | None = ...,
    residual: Incomplete | None = ...,
): ...
def minimum_node_cut(
    G,
    s: Incomplete | None = ...,
    t: Incomplete | None = ...,
    flow_func: Incomplete | None = ...,
): ...
def minimum_edge_cut(
    G,
    s: Incomplete | None = ...,
    t: Incomplete | None = ...,
    flow_func: Incomplete | None = ...,
): ...
