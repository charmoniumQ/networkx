from _typeshed import Incomplete

from .flow_func import _FlowFunc

default_flow_func: _FlowFunc = ...

def maximum_flow(
    flowG, _s, _t, capacity: str = ..., flow_func: Incomplete | None = ..., **kwargs
): ...
def maximum_flow_value(
    flowG, _s, _t, capacity: str = ..., flow_func: Incomplete | None = ..., **kwargs
): ...
def minimum_cut(
    flowG, _s, _t, capacity: str = ..., flow_func: Incomplete | None = ..., **kwargs
): ...
def minimum_cut_value(
    flowG, _s, _t, capacity: str = ..., flow_func: Incomplete | None = ..., **kwargs
): ...
