from random import randint


def Generate_Graph(n: int, d: int) -> dict:
    """Generate a random graph

    Args:
        n (int): Number of vertices
        d (int): Density

    Returns:
        dict: Graph
    """
    lb = 0
    ub = n * (n - 1) >> 1
    p = d * (ub + 1)
    G = {i: [] for i in range(1, n + 1)}
    for j in range(1, n + 1):
        for k in range(j + 1, n + 1):
            rnd = randint(lb, ub)
            if (k not in G[j]) and rnd < p:
                G[j].append(k)
                G[k].append(j)
    return G