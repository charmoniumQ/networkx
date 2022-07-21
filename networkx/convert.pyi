from typing import Dict, Iterable, Any, Union
from typing_extensions import TypeAlias
from _typeshed import Incomplete

from networkx.classes.graph import _EdgePlus, Graph, _Node

import numpy  # type: ignore
import scipy  # type: ignore

_Data = Union[
    Graph[_Node],
    Dict[_Node, Dict[_Node, Dict[str, Any]]],
    Dict[_Node, Iterable[_Node]],
    Iterable[_EdgePlus[_Node]],
    numpy.ndarray,
    scipy.sparse.base.spmatrix,
]

def to_networkx_graph(data, create_using: Incomplete | None = None, multigraph_input: bool = False): ...
def to_dict_of_lists(G, nodelist: Incomplete | None = ...): ...
def from_dict_of_lists(d, create_using: Incomplete | None = ...): ...
def to_dict_of_dicts(G, nodelist: Incomplete | None = ..., edge_data: Incomplete | None = ...): ...
def from_dict_of_dicts(d, create_using: Incomplete | None = ..., multigraph_input: bool = False): ...
def to_edgelist(G, nodelist: Incomplete | None = ...): ...
def from_edgelist(edgelist, create_using: Incomplete | None = ...): ...
