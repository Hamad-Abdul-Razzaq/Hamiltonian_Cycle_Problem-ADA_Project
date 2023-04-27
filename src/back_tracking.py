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


def HC_Check(G: int, path: list, current_pos: int, n:int) -> bool:
    if current_pos == n:
        if path[0] in G[path[current_pos - 1]]:
            return True
        else:
            return False
    
    for v in range(1, n+1):
        if v in G[path[current_pos - 1]] and not(v in path):
            path[current_pos] = v
            if HC_Check(G, path, current_pos + 1, n):
                return True
            else:
                path[current_pos] = -1
    return False

def HC_BT(G: int, n: int) -> bool:
    path = [-1 for _ in range(1,n+1)]
    path[0] = 1
    return HC_Check(G, path, 1, n)
def driver_code():
    vlb = 1
    vub = 6
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
                HC_BT(G, v)
                stop_time = perf_counter()
                total_time += (stop_time - start_time)
            f[(v, d)] = total_time/total_iter
            if f[(v, d)] > max:
                max = f[(v, d)]
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