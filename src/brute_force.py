from random import randint
import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt
# def permute(all_lst: list, lst: list, l: int, r: int, n:int, G:dict): # Find all graphs with node "n" that makes up the hamiltonian cycle
#     if l == r:
#         all_lst.append(lst.copy())
#         return BruteForce_HamiltonianCycle(G, n, lst)
#     else:
#         for i in range(l,r):
#             lst[l], lst[i] = lst[i], lst[l]
#             if permute(all_lst, lst, l+1, r, n, G) == True:
#                 return True
#             lst[l], lst[i] = lst[i], lst[l]


# def Generate_Graph(type: int, V:int):
#     G = dict()
#     if type == 0: # Generate complete graph (best case)
#         for n in range(1,V+1):
#             G = {i: [] for i in range(1,n+1)}
#             for j in range(1, n+1):
#                 for k in range(j+1, n+1):
#                     if (k not in G[j]):
#                         G[j].append(k)
#                         G[k].append(j)
#     elif type == 1: # Generate random graph (average/worst case)
#         for n in range(1,V+1):
#             G = {i: [] for i in range(1,n+1)}
#             for j in range(1, n+1):
#                 for k in range(j+1, n+1):
#                     if randint(0,1) == 1:
#                         if (k not in G[j]):
#                             G[j].append(k)
#                             G[k].append(j)
#     return G
    


# def BruteForce_HamiltonianCycle(G: dict, n: int, lst:list): # check if the edges in a permutation is present in the actual graph or not
#         # all_combinations = []
#         # lst = list(range(2, n+1))
#         # permute(all_combinations, lst, 0, n-1, n)
#     Path_exist = True
#     lst.insert(0, 1)
#     for j in range(1, len(lst)+1):
#         if j == len(lst) and j in G[1]:
#             break
#         elif j+1 not in G[j]:
#             Path_exist = False
#             break
#     if Path_exist:
#         # print("Hamiltonian Cycle Found !")
#         # print(lst)
#         # print(G)
#         return True
#     return False


# V_l = 1
# V_u = 6
# cg = []
# rg = []
# for n in range(V_l,V_u+1):
#     all_combinations = []
#     lst = list(range(2, n+1))
#     lst2 = lst.copy()
#     G = Generate_Graph(0, n)
#     a = perf_counter()
#     if permute(all_combinations, lst, 0, n-1, n, G):
#         print("Cycle Found! for n =", n, " (Complete Graph)")
#     else:
#         print("Cycle Not Found! for n =", n, " (Complete Graph)")
#     b = perf_counter()
#     cg.append(b-a)
#     G = Generate_Graph(1, n)
#     a = perf_counter()
#     if permute(all_combinations, lst2, 0, n-1, n, G):
#         print("Cycle Found! for n =", n, " (Randomized Graph)")
#     else:
#         print("Cycle Not Found! for n =", n, " (Randomized Graph)")

#     b = perf_counter()
#     rg.append(b-a)
# print(cg)
# print(rg)

# cgf = [0.0005448000001706532, 0.0015295000002879533, 0.0012784000000465312, 0.0012435999997251201, 0.0014826999999968393, 0.0014458999999078515, 0.003106099999968137, 0.002625600000101258, 0.002559599999585771]
# rgf = [0.0004967999998370942, 0.00045560000035038684, 0.0004473999997571809, 0.0004546000000118511, 0.0006035999999767228, 0.0009657999999035383, 0.004682999999658932, 0.12895280000020648, 7.954753600000004]
# plt.plot(list(range(1,len(cgf)+1)), cgf)
# plt.plot(list(range(1,len(cgf)+1)), rgf)
# plt.legend(["Best Case", "Worst Case"])
# plt.show()
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([7, 8, 9, 10, 11])
c = np.array([13, 14, 15, 16, 17, 18])
# X, Y = np.meshgrid(a, b)
X = np.array( [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]] )
Y = np.array( [[7 for _ in range(6)], [8 for _ in range(6)], [9 for _ in range(6)], [10 for _ in range(6)], [11 for _ in range(6)]] )
print(X)
print(Y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
print(Z)
ax = plt.axes(projection = "3d")
# ax.plot3D(a, b, c)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('Surface')
# X = np.array( [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]] )
plt.show()
