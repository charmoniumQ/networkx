from _typeshed import Incomplete
from collections.abc import Generator

def generate_adjlist(G, delimiter: str = ...) -> Generator[Incomplete, None, None]: ...
def write_adjlist(
    G, path, comments: str = ..., delimiter: str = ..., encoding: str = ...
) -> None: ...
def parse_adjlist(
    lines,
    comments: str = ...,
    delimiter: Incomplete | None = ...,
    create_using: Incomplete | None = ...,
    nodetype: Incomplete | None = ...,
): ...
def read_adjlist(
    path,
    comments: str = ...,
    delimiter: Incomplete | None = ...,
    create_using: Incomplete | None = ...,
    nodetype: Incomplete | None = ...,
    encoding: str = ...,
): ...
