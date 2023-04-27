from itertools import chain, combinations

from driver import driver_code
from generate_graph import Generate_Graph


def HC_DP(G: int, n: int) -> bool:
    """Dynamic programming algorithm to check if a hamiltonian cycle exists

    Args:
        G (int): Graph
        n (int): Number of vertices

    Returns:
        bool: True if hamiltonian cycle exists, False otherwise
    """
    x = range(1, n + 1)
    subsets = list(
        chain.from_iterable(combinations(x, r) for r in range(len(x) + 1)))
    MEMO = dict()
    for S in subsets:
        for u in S:
            if len(S) == 1:
                MEMO[(u, S)] = True
            else:
                S_prime = list(S)
                S_prime.remove(u)
                S_prime = tuple(S_prime)
                cycle_exist = True
                for v in S_prime:
                    if v in G[u] and MEMO.get((v, S_prime), False):
                        pass
                    else:
                        cycle_exist = False
                        break
                MEMO[(u, S)] = cycle_exist
    return any(MEMO[(v, tuple(x))] for v in x)


driver_code(HC_DP)
