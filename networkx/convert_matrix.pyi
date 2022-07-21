from _typeshed import Incomplete

def to_pandas_adjacency(
    G,
    nodelist: Incomplete | None = ...,
    dtype: Incomplete | None = ...,
    order: Incomplete | None = ...,
    multigraph_weight=...,
    weight: str = ...,
    nonedge: float = ...,
): ...
def from_pandas_adjacency(df, create_using: Incomplete | None = ...): ...
def to_pandas_edgelist(
    G,
    source: str = ...,
    target: str = ...,
    nodelist: Incomplete | None = ...,
    dtype: Incomplete | None = ...,
    edge_key: Incomplete | None = ...,
): ...
def from_pandas_edgelist(
    df,
    source: str = ...,
    target: str = ...,
    edge_attr: Incomplete | None = ...,
    create_using: Incomplete | None = ...,
    edge_key: Incomplete | None = ...,
): ...
def to_scipy_sparse_array(
    G,
    nodelist: Incomplete | None = ...,
    dtype: Incomplete | None = ...,
    weight: str = ...,
    format: str = ...,
): ...
def from_scipy_sparse_array(
    A,
    parallel_edges: bool = ...,
    create_using: Incomplete | None = ...,
    edge_attribute: str = ...,
): ...
def to_numpy_array(
    G,
    nodelist: Incomplete | None = ...,
    dtype: Incomplete | None = ...,
    order: Incomplete | None = ...,
    multigraph_weight=...,
    weight: str = ...,
    nonedge: float = ...,
): ...
def from_numpy_array(
    A, parallel_edges: bool = ..., create_using: Incomplete | None = ...
): ...
