from itertools import chain, combinations
from random import randint
from time import perf_counter
import numpy as np
import matplotlib.pyplot as plt

def Generate_Graph(n: int, d: int) -> dict:
    lb = 0
    ub = n*(n-1)/2
    p = d*(ub+1)
    G = {i: [] for i in range(1,n+1)}
    for j in range(1, n+1):
        for k in range(j+1, n+1):
            rnd = randint(lb, ub)
            if (k not in G[j]):
                if rnd < p:    
                    G[j].append(k)
                    G[k].append(j)
    return G

def HC_DP(G: int, n: int) -> bool:
    x = range(1,n+1)
    subsets = list(chain.from_iterable(combinations(x,r) for r in range(len(x)+1)))
    MEMO = dict()
    for S in subsets:
        for u in S:
            if len(S) == 1:
                MEMO[(u,S)] = True
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
                MEMO[(u,S)] = cycle_exist
    for v in x:
        if MEMO[(v, tuple(x))]:
            return True
    return False

def driver_code():
    vlb = 8
    vub = 8
    f = dict()
    x = list(range(vlb, vub+1))
    y = [round(0.05*i, 2) for i in range(0,21)]
    max = 0
    for v in x:
        for d in y:
            total_time = 0
            total_iter = 1000
            for _ in range(total_iter):
                G = Generate_Graph(v, d)
                start_time = perf_counter()
                HC_DP(G, v)
                stop_time = perf_counter()
                total_time += (stop_time - start_time)
            f[(v, d)] = total_time/total_iter
            if f[(v, d)] > max:
                max = f[(v, d)]
    print(max)
    X = np.array(list(list(i for i in range(vlb, vub+1)) for _ in range(len(y))))
    Y = np.array(list(list(i for j in range(vlb, vub+1)) for i in y))
    Z = np.array(list(list(0.0005 for _ in range(vlb, vub+1)) for _ in range(len(y))))
    # print(f)
    for i in range(len(y)):
        for j in range(len(x)):
            Z[i][j] = f[(X[i][j], Y[i][j])]
    # print(X)
    # print(Y)
    # print(Z)
    print(f)
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title("Hamiltoniain Cycle - Dynamic Programming")
    ax.invert_xaxis()
    ax.set_xlabel("Number of Vertices")
    ax.set_ylabel("Graph Density")
    ax.set_zlabel("Time Taken")
    plt.show()

driver_code()
# G = {1: [2, 4], 2: [1, 3, 4], 3: [2, 4], 4: [1, 2, 3]}
# print(HC_DP(G, 4))