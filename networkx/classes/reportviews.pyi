from _typeshed import Incomplete
from collections.abc import Mapping, Set

class NodeView(Mapping, Set):
    def __init__(self, graph) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, n): ...
    def __contains__(self, n): ...
    def __call__(self, data: bool = ..., default: Incomplete | None = ...): ...
    def data(self, data: bool = ..., default: Incomplete | None = ...): ...

class NodeDataView(Set):
    def __init__(self, nodedict, data: bool = ..., default: Incomplete | None = ...) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __contains__(self, n): ...
    def __getitem__(self, n): ...

class DiDegreeView:
    def __init__(self, G, nbunch: Incomplete | None = ..., weight: Incomplete | None = ...) -> None: ...
    def __call__(self, nbunch: Incomplete | None = ..., weight: Incomplete | None = ...): ...
    def __getitem__(self, n): ...
    def __iter__(self): ...
    def __len__(self): ...

class DegreeView(DiDegreeView):
    def __getitem__(self, n): ...
    def __iter__(self): ...

class OutDegreeView(DiDegreeView):
    def __getitem__(self, n): ...
    def __iter__(self): ...

class InDegreeView(DiDegreeView):
    def __getitem__(self, n): ...
    def __iter__(self): ...

class MultiDegreeView(DiDegreeView):
    def __getitem__(self, n): ...
    def __iter__(self): ...

class DiMultiDegreeView(DiDegreeView):
    def __getitem__(self, n): ...
    def __iter__(self): ...

class InMultiDegreeView(DiDegreeView):
    def __getitem__(self, n): ...
    def __iter__(self): ...

class OutMultiDegreeView(DiDegreeView):
    def __getitem__(self, n): ...
    def __iter__(self): ...

class OutEdgeDataView:
    def __init__(self, viewer, nbunch: Incomplete | None = ..., data: bool = ..., default: Incomplete | None = ...): ...
    def __len__(self): ...
    def __iter__(self): ...
    def __contains__(self, e): ...

class EdgeDataView(OutEdgeDataView):
    def __len__(self): ...
    def __iter__(self): ...
    def __contains__(self, e): ...

class InEdgeDataView(OutEdgeDataView):
    def __iter__(self): ...
    def __contains__(self, e): ...

class OutMultiEdgeDataView(OutEdgeDataView):
    keys: Incomplete
    def __init__(self, viewer, nbunch: Incomplete | None = ..., data: bool = ..., keys: bool = ..., default: Incomplete | None = ...): ...
    def __len__(self): ...
    def __iter__(self): ...
    def __contains__(self, e): ...

class MultiEdgeDataView(OutMultiEdgeDataView):
    def __iter__(self): ...
    def __contains__(self, e): ...

class InMultiEdgeDataView(OutMultiEdgeDataView):
    def __iter__(self): ...
    def __contains__(self, e): ...

class OutEdgeView(Set, Mapping):
    dataview: Incomplete
    def __init__(self, G) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __contains__(self, e): ...
    def __getitem__(self, e): ...
    def __call__(self, nbunch: Incomplete | None = ..., data: bool = ..., default: Incomplete | None = ...): ...
    def data(self, data: bool = ..., default: Incomplete | None = ..., nbunch: Incomplete | None = ...): ...

class EdgeView(OutEdgeView):
    dataview: Incomplete
    def __len__(self): ...
    def __iter__(self): ...
    def __contains__(self, e): ...

class InEdgeView(OutEdgeView):
    dataview: Incomplete
    def __init__(self, G) -> None: ...
    def __iter__(self): ...
    def __contains__(self, e): ...
    def __getitem__(self, e): ...

class OutMultiEdgeView(OutEdgeView):
    dataview: Incomplete
    def __len__(self): ...
    def __iter__(self): ...
    def __contains__(self, e): ...
    def __getitem__(self, e): ...
    def __call__(self, nbunch: Incomplete | None = ..., data: bool = ..., keys: bool = ..., default: Incomplete | None = ...): ...
    def data(self, data: bool = ..., keys: bool = ..., default: Incomplete | None = ..., nbunch: Incomplete | None = ...): ...

class MultiEdgeView(OutMultiEdgeView):
    dataview: Incomplete
    def __len__(self): ...
    def __iter__(self): ...

class InMultiEdgeView(OutMultiEdgeView):
    dataview: Incomplete
    def __init__(self, G) -> None: ...
    def __iter__(self): ...
    def __contains__(self, e): ...
    def __getitem__(self, e): ...
