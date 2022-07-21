from typing import Protocol
from _typeshed import Incomplete

class _FlowFunc(Protocol):
    def __call__(
            self,
            G,
            s,
            t,
            capacity: str = ...,
            residual: Incomplete | None = ...,
            value_only: bool = ...,
    ): ...
