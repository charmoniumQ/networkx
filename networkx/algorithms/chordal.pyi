from collections.abc import Generator

from _typeshed import Incomplete

import networkx as nx

class NetworkXTreewidthBoundExceeded(nx.NetworkXException): ...

def is_chordal(G): ...
def find_induced_nodes(G, s, t, treewidth_bound=...): ...
def chordal_graph_cliques(G) -> Generator[Incomplete, None, None]: ...
def chordal_graph_treewidth(G): ...
def complete_to_chordal_graph(G): ...
