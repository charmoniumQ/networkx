from _typeshed import Incomplete

def equivalence_classes(iterable, relation): ...
def quotient_graph(
    G,
    partition,
    edge_relation: Incomplete | None = ...,
    node_data: Incomplete | None = ...,
    edge_data: Incomplete | None = ...,
    relabel: bool = ...,
    create_using: Incomplete | None = ...,
): ...
def contracted_nodes(G, u, v, self_loops: bool = ..., copy: bool = ...): ...

identified_nodes = contracted_nodes

def contracted_edge(G, edge, self_loops: bool = ..., copy: bool = ...): ...
