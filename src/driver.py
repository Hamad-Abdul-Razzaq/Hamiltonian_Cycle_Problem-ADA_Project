from time import perf_counter

import matplotlib.pyplot as plt
import numpy as np

from generate_graph import Generate_Graph


def driver_code(func):
    vlb = 1
    vub = 5
    f = dict()
    x = list(range(vlb, vub + 1))
    y = [round(0.05 * i, 2) for i in range(0, 21)]
    max_ = 0
    for v in x:
        for d in y:
            total_time = 0
            total_iter = 1000
            for _ in range(total_iter):
                G = Generate_Graph(v, d)
                start_time = perf_counter()
                func(G, v)
                stop_time = perf_counter()
                total_time += stop_time - start_time
            f[(v, d)] = total_time / total_iter
            if f[(v, d)] > max_:
                max_ = f[(v, d)]
    X = np.array(
        list(list(i for i in range(vlb, vub + 1)) for _ in range(len(y))))
    Y = np.array(list(list(i for j in range(vlb, vub + 1)) for i in y))
    Z = np.array(
        list(list(0.0005 for _ in range(vlb, vub + 1)) for _ in range(len(y))))

    for i in range(len(y)):
        for j in range(len(x)):
            Z[i][j] = f[(X[i][j], Y[i][j])]
    print(f)
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot_surface(X,
                    Y,
                    Z,
                    rstride=1,
                    cstride=1,
                    cmap="viridis",
                    edgecolor="none")
    ax.set_title("Hamiltoniain Cycle - Dynamic Programming")
    ax.invert_xaxis()
    ax.set_xlabel("Number of Vertices")
    ax.set_ylabel("Graph Density")
    ax.set_zlabel("Time Taken")
    plt.show()