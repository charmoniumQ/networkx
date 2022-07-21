from collections.abc import Generator

from _typeshed import Incomplete

class GraphMatcher:
    G1: Incomplete
    G2: Incomplete
    G1_nodes: Incomplete
    G2_nodes: Incomplete
    G2_node_order: Incomplete
    old_recursion_limit: Incomplete
    test: str
    def __init__(self, G1, G2) -> None: ...
    def reset_recursion_limit(self) -> None: ...
    def candidate_pairs_iter(self) -> Generator[Incomplete, None, None]: ...
    core_1: Incomplete
    core_2: Incomplete
    inout_1: Incomplete
    inout_2: Incomplete
    state: Incomplete
    mapping: Incomplete
    def initialize(self) -> None: ...
    def is_isomorphic(self): ...
    def isomorphisms_iter(self) -> None: ...
    def match(self) -> Generator[Incomplete, None, None]: ...
    def semantic_feasibility(self, G1_node, G2_node): ...
    def subgraph_is_isomorphic(self): ...
    def subgraph_is_monomorphic(self): ...
    def subgraph_isomorphisms_iter(self) -> None: ...
    def subgraph_monomorphisms_iter(self) -> None: ...
    def syntactic_feasibility(self, G1_node, G2_node): ...

class DiGraphMatcher(GraphMatcher):
    def __init__(self, G1, G2) -> None: ...
    def candidate_pairs_iter(self) -> Generator[Incomplete, None, None]: ...
    core_1: Incomplete
    core_2: Incomplete
    in_1: Incomplete
    in_2: Incomplete
    out_1: Incomplete
    out_2: Incomplete
    state: Incomplete
    mapping: Incomplete
    def initialize(self) -> None: ...
    def syntactic_feasibility(self, G1_node, G2_node): ...

class GMState:
    GM: Incomplete
    G1_node: Incomplete
    G2_node: Incomplete
    depth: Incomplete
    def __init__(
        self, GM, G1_node: Incomplete | None = ..., G2_node: Incomplete | None = ...
    ) -> None: ...
    def restore(self) -> None: ...

class DiGMState:
    GM: Incomplete
    G1_node: Incomplete
    G2_node: Incomplete
    depth: Incomplete
    def __init__(
        self, GM, G1_node: Incomplete | None = ..., G2_node: Incomplete | None = ...
    ) -> None: ...
    def restore(self) -> None: ...
