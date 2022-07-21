from _typeshed import Incomplete
from collections.abc import Generator

def is_simple_path(G, nodes): ...
def all_simple_paths(G, source, target, cutoff: Incomplete | None = ...): ...
def all_simple_edge_paths(G, source, target, cutoff: Incomplete | None = ...) -> Generator[Incomplete, None, Incomplete]: ...
def shortest_simple_paths(G, source, target, weight: Incomplete | None = ...) -> Generator[Incomplete, None, Incomplete]: ...
def _bidirectional_shortest_path(G, source, target, weight: Incomplete | None = None): ...
def _bidirectional_dijkstra(G, source, target, weight: Incomplete | None = ..., ignore_nodes: Incomplete | None = None, ignore_edges: Incomplete | None = None): ...

class PathBuffer:
    paths: Incomplete
    sortedpaths: Incomplete
    counter: Incomplete
    def __init__(self) -> None: ...
    def __len__(self): ...
    def push(self, cost, path) -> None: ...
    def pop(self): ...
