import networkx as nx
from _typeshed import Incomplete

def branching_weight(G, attr: str = ..., default: int = ...): ...
def greedy_branching(
    G,
    attr: str = ...,
    default: int = ...,
    kind: str = ...,
    seed: Incomplete | None = ...,
): ...

class MultiDiGraph_EdgeKey(nx.MultiDiGraph):
    edge_index: Incomplete
    def __init__(
        self, incoming_graph_data: Incomplete | None = ..., **attr
    ) -> None: ...
    def remove_node(self, n) -> None: ...
    def remove_nodes_from(self, nbunch) -> None: ...
    def add_edge(self, u_for_edge, v_for_edge, key_for_edge, **attr) -> None: ...  # type: ignore
    def add_edges_from(self, ebunch_to_add, **attr) -> None: ...
    def remove_edge_with_key(self, key) -> None: ...
    def remove_edges_from(self, ebunch) -> None: ...

class Edmonds:
    G_original: Incomplete
    store: bool
    edges: Incomplete
    template: Incomplete
    def __init__(self, G, seed: Incomplete | None = ...) -> None: ...
    def find_optimum(
        self,
        attr: str = ...,
        default: int = ...,
        kind: str = ...,
        style: str = ...,
        preserve_attrs: bool = ...,
        partition: Incomplete | None = ...,
        seed: Incomplete | None = ...,
    ): ...

def maximum_branching(
    G,
    attr: str = ...,
    default: int = ...,
    preserve_attrs: bool = ...,
    partition: Incomplete | None = ...,
): ...
def minimum_branching(
    G,
    attr: str = ...,
    default: int = ...,
    preserve_attrs: bool = ...,
    partition: Incomplete | None = ...,
): ...
def maximum_spanning_arborescence(
    G,
    attr: str = ...,
    default: int = ...,
    preserve_attrs: bool = ...,
    partition: Incomplete | None = ...,
): ...
def minimum_spanning_arborescence(
    G,
    attr: str = ...,
    default: int = ...,
    preserve_attrs: bool = ...,
    partition: Incomplete | None = ...,
): ...

class ArborescenceIterator:
    class Partition:
        mst_weight: float
        partition_dict: dict
        def __copy__(self): ...
        def __init__(self, mst_weight, partition_dict) -> None: ...
        def __lt__(self, other): ...
        def __gt__(self, other): ...
        def __le__(self, other): ...
        def __ge__(self, other): ...
    G: Incomplete
    weight: Incomplete
    minimum: Incomplete
    method: Incomplete
    partition_key: str
    init_partition: Incomplete
    def __init__(
        self,
        G,
        weight: str = ...,
        minimum: bool = ...,
        init_partition: Incomplete | None = ...,
    ) -> None: ...
    partition_queue: Incomplete
    def __iter__(self): ...
    def __next__(self): ...
