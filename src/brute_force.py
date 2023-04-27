from driver import driver_code
from generate_graph import Generate_Graph


def permute_and_check(all_lst: list, lst: list, l: int, r: int, n: int,
                      G: dict) -> bool:
    """Generate all permutations of a list and check if it is a hamiltonian cycle

    Args:
        all_lst (list): List of all permutations
        lst (list): List of all vertices
        l (int): Left index
        r (int): Right index
        n (int): Number of vertices
        G (dict): Graph

    Returns:
        bool: True if hamiltonian cycle exists, False otherwise
    """
    if l == r:
        all_lst.append(lst.copy())
        return HC_Check(G, n, lst)

    for i in range(l, r):
        lst[l], lst[i] = lst[i], lst[l]
        if permute_and_check(all_lst, lst, l + 1, r, n, G):
            return True
        lst[l], lst[i] = lst[i], lst[l]
    return False


def HC_BF(G: dict, n: int) -> bool:
    """Brute force algorithm to check if a hamiltonian cycle exists

    Args:
        G (dict): Graph
        n (int): Number of vertices

    Returns:
        bool: True if hamiltonian cycle exists, False otherwise
    """
    all_combinations = list()
    lst = list(range(2, n + 1))
    return permute_and_check(all_combinations, lst, 0, n - 1, n, G)


def HC_Check(G: dict, n: int, lst: list) -> bool:
    """Check if a hamiltonian cycle exists

    Args:
        G (dict): Graph
        n (int): Number of vertices
        lst (list): List of all vertices

    Returns:
        bool: True if hamiltonian cycle exists, False otherwise
    """
    Path_exist = True
    lst.insert(0, 1)
    for j in range(1, len(lst) + 1):
        if j == len(lst) and j in G[1]:
            break
        elif j + 1 not in G[j]:
            Path_exist = False
            break
    return Path_exist


driver_code(HC_BF)