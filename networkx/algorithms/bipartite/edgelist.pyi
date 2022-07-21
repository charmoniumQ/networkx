from collections.abc import Generator

from _typeshed import Incomplete

def write_edgelist(
    G,
    path,
    comments: str = ...,
    delimiter: str = ...,
    data: bool = ...,
    encoding: str = ...,
) -> None: ...
def generate_edgelist(
    G, delimiter: str = ..., data: bool = ...
) -> Generator[Incomplete, None, None]: ...
def parse_edgelist(
    lines,
    comments: str = ...,
    delimiter: Incomplete | None = ...,
    create_using: Incomplete | None = ...,
    nodetype: Incomplete | None = ...,
    data: bool = ...,
): ...
def read_edgelist(
    path,
    comments: str = ...,
    delimiter: Incomplete | None = ...,
    create_using: Incomplete | None = ...,
    nodetype: Incomplete | None = ...,
    data: bool = ...,
    edgetype: Incomplete | None = ...,
    encoding: str = ...,
): ...
