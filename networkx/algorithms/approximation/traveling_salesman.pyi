from _typeshed import Incomplete

def christofides(G, weight: str = ..., tree: Incomplete | None = ...): ...
def traveling_salesman_problem(
    G,
    weight: str = ...,
    nodes: Incomplete | None = ...,
    cycle: bool = ...,
    method: Incomplete | None = ...,
): ...
def asadpour_atsp(
    G, weight: str = ..., seed: Incomplete | None = ..., source: Incomplete | None = ...
): ...
def greedy_tsp(G, weight: str = ..., source: Incomplete | None = ...): ...
def simulated_annealing_tsp(
    G,
    init_cycle,
    weight: str = ...,
    source: Incomplete | None = ...,
    temp: int = ...,
    move: str = ...,
    max_iterations: int = ...,
    N_inner: int = ...,
    alpha: float = ...,
    seed: Incomplete | None = ...,
): ...
def threshold_accepting_tsp(
    G,
    init_cycle,
    weight: str = ...,
    source: Incomplete | None = ...,
    threshold: int = ...,
    move: str = ...,
    max_iterations: int = ...,
    N_inner: int = ...,
    alpha: float = ...,
    seed: Incomplete | None = ...,
): ...
