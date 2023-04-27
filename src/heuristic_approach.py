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


def rotational_transformation(path: list, G: dict) -> list:
    e = path[-1]
    b = None
    for j in path:
        if j in G[e] and j!= path[-2]:
            b = j
    if b == None:
        return []
    else:
        new_path = []
        idx = 0
        for i in path:
            new_path.append(i)
            if i == b:
                break
            idx += 1
        new_path.extend(path[len(path)-1:idx:-1])
        if new_path == path:
            return []
        else:
            return new_path


def unreachable(path: list, v: int, G:int) -> bool:
    for i in G[v]:
        if not(i in path) :
            reachable = False
            for j in G[i]:
                if not(j in path) :
                    reachable = True
            if not(reachable):
                return True
    return False

def PhaseI(G: int, n:int, Va: list, Vd: list, idx: int, path: list) -> list:
    vs = Vd[idx][0]
    if not(vs in path):
        path.append(vs)
    # print("in", path)
    i = 0
    while i < len(Va):
        if Va[i][0] in G[path[-1]]:
            vi = Va[i][0]
            # print(not(unreachable(path, vi, G)), vi, path)
            if not(unreachable(path, vi, G)) and not (vi in path):
                path.append(vi)
                vs = vi
                i += 1
            else:
                i += 1
        else:
            i += 1
    return path

def PhaseIII(G: dict, deg: dict, P: list) -> bool:
    done_so_far = [P.copy()]
    while True:
        # print("MF3")
        if P[0] in G[P[-1]]:
            # print(P)
            return True
        if deg[P[0]] > deg[P[-1]]:
            P.reverse()
        P = rotational_transformation(P, G)
        if P in done_so_far:
            return False
        else:
            done_so_far.append(P)
        # print('r',P)
        if P == []:
            return False
        

def HC_HA(G: int, n: int) -> bool:
    deg = {i:len(G[i]) for i in G}
    Va = list(deg.items())
    for i in range(len(Va)):
        for j in range(len(Va)-i-1):
            if Va[j][1] > Va[j+1][1]:
                tmp = Va[j+1]
                Va[j+1] = Va[j]
                Va[j] = tmp
    Vd = Va.copy()
    Vd.reverse()
    idx = 0
    path = []
    PhaseI(G, n, Va, Vd, idx, path)
    # print('l', path)
    if len(path) == n:
        return PhaseIII(G, deg, path)
    else:
        max_ = path.copy()
        sz = len(path)
        for i in range(len(Vd)):
            tmp = []
            # print("Once")
            path = PhaseI(G, n, Va, Vd, i, tmp)
            # print('l', path)
            if len(path) > sz:
                max_ = path.copy()
                sz = len(max_)
        P = max_
        # print("l", P)
        done_so_far = [P.copy()]
        while len(P) != n:
            if deg[P[0]] > deg[P[-1]]:
                P.reverse()
            P = rotational_transformation(P, G)
            if P in done_so_far:
                return False
            else:
                done_so_far.append(P)
            # print("r", P)
            if P == []:
                # print("return it")
                return False
            else:
                # print(P)
                PhaseI(G, n, Va, Vd, 0, P)
        # print("f", P)
        Ph = P.copy()
        if Ph[0] in G[Ph[-1]]:
            # print(Ph)
            return True
        else:
            return PhaseIII(G, deg, Ph)
        
        





def driver_code():
    vlb = 8
    vub = 12
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
                HC_HA(G, v)
                stop_time = perf_counter()
                total_time += (stop_time - start_time)
            f[(v, d)] = total_time/total_iter
            if f[(v, d)] > max:
                max = f[(v, d)]
    print(max)
    X = np.array(list(list(i for i in range(vlb, vub+1)) for _ in range(len(y))))
    Y = np.array(list(list(i for j in range(vlb, vub+1)) for i in y))
    Z = np.array(list(list(0.0005 for _ in range(vlb, vub+1)) for _ in range(len(y))))
    print(f)
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

# G = Generate_Graph(3, 0.4)
# print(G)
# print(HC_HA(G, 3))