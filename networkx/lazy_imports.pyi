import types

from _typeshed import Incomplete

def attach(
    module_name,
    submodules: Incomplete | None = ...,
    submod_attrs: Incomplete | None = ...,
): ...
def _lazy_import(fullname): ...

class DelayedImportErrorModule(types.ModuleType):
    def __init__(self, frame_data, *args, **kwargs) -> None: ...
    def __getattr__(self, x) -> None: ...
