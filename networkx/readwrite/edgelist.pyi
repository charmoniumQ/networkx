from collections.abc import Generator

from _typeshed import Incomplete

def generate_edgelist(
    G, delimiter: str = ..., data: bool = ...
) -> Generator[Incomplete, None, None]: ...
def write_edgelist(
    G,
    path,
    comments: str = ...,
    delimiter: str = ...,
    data: bool = ...,
    encoding: str = ...,
) -> None: ...
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
def write_weighted_edgelist(
    G, path, comments: str = ..., delimiter: str = ..., encoding: str = ...
) -> None: ...
def read_weighted_edgelist(
    path,
    comments: str = ...,
    delimiter: Incomplete | None = ...,
    create_using: Incomplete | None = ...,
    nodetype: Incomplete | None = ...,
    encoding: str = ...,
): ...
