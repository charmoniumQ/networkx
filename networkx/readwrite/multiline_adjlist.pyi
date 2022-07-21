from collections.abc import Generator

from _typeshed import Incomplete

def generate_multiline_adjlist(
    G, delimiter: str = ...
) -> Generator[Incomplete, None, None]: ...
def write_multiline_adjlist(
    G, path, delimiter: str = ..., comments: str = ..., encoding: str = ...
) -> None: ...
def parse_multiline_adjlist(
    lines,
    comments: str = ...,
    delimiter: Incomplete | None = ...,
    create_using: Incomplete | None = ...,
    nodetype: Incomplete | None = ...,
    edgetype: Incomplete | None = ...,
): ...
def read_multiline_adjlist(
    path,
    comments: str = ...,
    delimiter: Incomplete | None = ...,
    create_using: Incomplete | None = ...,
    nodetype: Incomplete | None = ...,
    edgetype: Incomplete | None = ...,
    encoding: str = ...,
): ...
