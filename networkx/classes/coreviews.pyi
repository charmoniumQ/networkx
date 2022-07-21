from typing import Any, Dict, Generic, Iterator, Mapping, Tuple, TypeVar

_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")

class AtlasView(Mapping[_T, Dict[_U, _V]], Generic[_T, _U, _V]):
    def __init__(self, d: Mapping[_T, Dict[_U, _V]]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, key: _T) -> Dict[_U, _V]: ...
    def copy(self) -> AtlasView: ...

class AdjacencyView(AtlasView[_T, _U, _V], Generic[_T, _U, _V]): ...
class MultiAdjacencyView(AdjacencyView): ...

class UnionAtlas(Mapping):
    def __init__(self, succ: Any, pred: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, key: Any): ...
    def copy(self): ...

class UnionAdjacency(Mapping):
    def __init__(self, succ: Any, pred: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, nbr: Any): ...
    def copy(self): ...

class UnionMultiInner(UnionAtlas):
    def __getitem__(self, node: Any): ...
    def copy(self): ...

class UnionMultiAdjacency(UnionAdjacency):
    def __getitem__(self, node: Any): ...

class FilterAtlas(Mapping):
    NODE_OK: Any = ...
    def __init__(self, d: Any, NODE_OK: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, key: Any): ...

class FilterAdjacency(Mapping):
    NODE_OK: Any = ...
    EDGE_OK: Any = ...
    def __init__(self, d: Any, NODE_OK: Any, EDGE_OK: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, node: Any): ...

class FilterMultiInner(FilterAdjacency):
    def __iter__(self): ...
    def __getitem__(self, nbr: Any): ...

class FilterMultiAdjacency(FilterAdjacency):
    def __getitem__(self, node: Any): ...