from .edmondskarp import edmonds_karp
from _typeshed import Incomplete
from .flow_func import _FlowFunc

default_flow_func: _FlowFunc

def gomory_hu_tree(G, capacity: str = ..., flow_func: Incomplete | None = ...): ...
