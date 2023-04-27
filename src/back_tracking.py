from itertools import chain, combinations

from driver import driver_code
from generate_graph import Generate_Graph


def HC_Check(G: int, path: list, current_pos: int, n: int) -> bool:
    """Check if a hamiltonian cycle exists

    Args:
        G (int): Graph
        path (list): List of all vertices
        current_pos (int): current position in path
        n (int): Number of vertices

    Returns:
        bool: True if hamiltonian cycle exists, False otherwise
    """
    if current_pos == n:
        return path[0] in G[path[current_pos - 1]]

    for v in range(1, n + 1):
        if v in G[path[current_pos - 1]] and not (v in path):
            path[current_pos] = v
            if HC_Check(G, path, current_pos + 1, n):
                return True
            else:
                path[current_pos] = -1
    return False


def HC_BT(G: int, n: int) -> bool:
    """Backtracking algorithm to check if a hamiltonian cycle exists

    Args:
        G (int): Graph
        n (int): Number of vertices

    Returns:
        bool: True if hamiltonian cycle exists, False otherwise
    """
    path = [-1 for _ in range(1, n + 1)]
    path[0] = 1
    return HC_Check(G, path, 1, n)


driver_code(HC_BT)
