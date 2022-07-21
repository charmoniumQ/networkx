from .preflowpush import preflow_push
from _typeshed import Incomplete

default_flow_func = preflow_push

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
