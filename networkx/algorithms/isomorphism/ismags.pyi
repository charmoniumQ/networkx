from collections.abc import Generator

from _typeshed import Incomplete

class ISMAGS:
    graph: Incomplete
    subgraph: Incomplete
    node_equality: Incomplete
    edge_equality: Incomplete
    def __init__(
        self,
        graph,
        subgraph,
        node_match: Incomplete | None = ...,
        edge_match: Incomplete | None = ...,
        cache: Incomplete | None = ...,
    ): ...
    def find_isomorphisms(
        self, symmetry: bool = ...
    ) -> Generator[Incomplete, None, Incomplete]: ...
    def largest_common_subgraph(
        self, symmetry: bool = ...
    ) -> Generator[Incomplete, None, None]: ...
    def analyze_symmetry(self, graph, node_partitions, edge_colors): ...
    def is_isomorphic(self, symmetry: bool = ...): ...
    def subgraph_is_isomorphic(self, symmetry: bool = ...): ...
    def isomorphisms_iter(self, symmetry: bool = ...) -> None: ...
    def subgraph_isomorphisms_iter(self, symmetry: bool = ...): ...
