from random import randint

def permute(all_lst: list, lst: list, l: int, r: int, n:int):
    if l == r:
        all_lst.append(lst.copy())
    else:
        for i in range(l,r):
            lst[l], lst[i] = lst[i], lst[l]
            permute(all_lst, lst, l+1, r, n)
            lst[l], lst[i] = lst[i], lst[l]


def Generate_Graph(type: int):
    if type == 0:
        for n in range(1,12):
            G = {i: [] for i in range(1,n+1)}
            for j in range(1, n+1):
                for k in range(j+1, n+1):
                    if (k not in G[j]):
                        G[j].append(k)
                        G[k].append(j)
    elif type == 1:
        for n in range(1,12):
            G = {i: [] for i in range(1,n+1)}
            for j in range(1, n+1):
                for k in range(j+1, n+1):
                    if randint(0,1) == 1:
                        if (k not in G[j]):
                            G[j].append(k)
                            G[k].append(j)
    return G
    


def BruteForce_HamiltonianCycle(G: dict, n: int):
        all_combinations = []
        lst = list(range(2, n+1))
        permute(all_combinations, lst, 0, n-1, n)
        Path_exist = True
        for lt in range(len(all_combinations)):
            all_combinations[lt].insert(0, 1)
            for j in range(1, len(all_combinations[lt])+1):
                if j == len(all_combinations[lt]) and j in G[1]:
                    break
                elif j+1 not in G[j]:
                    Path_exist = False
                    break
            if Path_exist:
                print("Hamiltonian Cycle Found !")
                print(all_combinations[lt])
                print(G)
                break
        print("No Hamiltonian Cycle Exists! for n =", n)


for n in range(1,11):
    G = Generate_Graph(0)
    BruteForce_HamiltonianCycle(G, n)
    G = Generate_Graph(1)
    BruteForce_HamiltonianCycle(G, n)