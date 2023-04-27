from random import randint
from time import perf_counter
import numpy as np
import matplotlib.pyplot as plt
# np.set_printoptions(precision=3)

def permute_and_check(all_lst: list, lst: list, l: int, r: int, n:int, G:dict) -> bool: # Find all graphs with node "n" that makes up the hamiltonian cycle
    if l == r:
        all_lst.append(lst.copy())
        return HC_Check(G, n, lst)
    else:
        for i in range(l,r):
            lst[l], lst[i] = lst[i], lst[l]
            if permute_and_check(all_lst, lst, l+1, r, n, G) == True:
                return True
            lst[l], lst[i] = lst[i], lst[l]
    return False


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

def HC_BF(G: dict, n: int) -> bool:
    all_combinations = list()
    lst = list(range(2, n+1))
    return permute_and_check(all_combinations, lst, 0, n-1, n, G)

def HC_Check(G: dict, n: int, lst:list):
    Path_exist = True
    lst.insert(0, 1)
    for j in range(1, len(lst)+1):
        if j == len(lst) and j in G[1]:
            break
        elif j+1 not in G[j]:
            Path_exist = False
            break
    if Path_exist:
        return True
    return False

def driver_code() -> None:
    vlb = 8
    vub = 8
    f = dict()
    x = list(range(vlb, vub+1))
    y = [round(0.05*i, 2) for i in range(0,21)]
    max = 0
    for v in x:
        for d in y:
            total_time = 0
            total_iter = 100
            print(v, d)
            for _ in range(total_iter):
                print(_)
                G = Generate_Graph(v, d)
                start_time = perf_counter()
                HC_BF(G, v)
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
    print(f)
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title("Hamiltoniain Cycle - Brute Force")
    ax.invert_xaxis()
    ax.set_xlabel("Number of Vertices")
    ax.set_ylabel("Graph Density")
    ax.set_zlabel("Time Taken")
    plt.show()
    
driver_code()
# G = {1: [2, 4], 2: [1, 3, 4], 3: [2, 4], 4: [1, 2, 3]}
# print(HC_BF(G, 4))
    