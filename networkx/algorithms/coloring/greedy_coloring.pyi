from collections.abc import Generator

from _typeshed import Incomplete

def strategy_largest_first(G, colors): ...
def strategy_random_sequential(G, colors, seed: Incomplete | None = ...): ...
def strategy_smallest_last(G, colors): ...
def strategy_independent_set(G, colors) -> None: ...
def strategy_connected_sequential_bfs(G, colors): ...
def strategy_connected_sequential_dfs(G, colors): ...
def strategy_connected_sequential(
    G, colors, traversal: str = ...
) -> Generator[Incomplete, None, None]: ...
def strategy_saturation_largest_first(
    G, colors
) -> Generator[Incomplete, None, Incomplete]: ...
def greedy_color(G, strategy: str = ..., interchange: bool = ...): ...

class _Node:
    node_id: Incomplete
    color: int
    adj_list: Incomplete
    adj_color: Incomplete
    def __init__(self, node_id, n) -> None: ...
    def assign_color(self, adj_entry, color) -> None: ...
    def clear_color(self, adj_entry, color) -> None: ...
    def iter_neighbors(self) -> Generator[Incomplete, None, None]: ...
    def iter_neighbors_color(self, color) -> Generator[Incomplete, None, None]: ...

class _AdjEntry:
    node_id: Incomplete
    next: Incomplete
    mate: Incomplete
    col_next: Incomplete
    col_prev: Incomplete
    def __init__(self, node_id) -> None: ...
