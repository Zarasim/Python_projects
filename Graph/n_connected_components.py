# graph with n nodes and array edges so that edge[i] = [a,b] indicates an edge. Returns n° connected components

# use dfs from first element to find a connected component. Since 1 has been already visited no need to increment connected components O(E + V)

# Union-Find increases the efficiency

# [[0,1],[1,2],[3,4]]

# par array = [0,1,2,3,4] they match the node Initially we have n trees
# Rank = [1,1,1,1,1] -> Rank = [2,1,1,1,1] merge 0 and 1

# Even if 2 is connected to 1 we connect it to the parent 0, so Rank = [3,1,1,1,1] Par = [0,0,0,3,4]

# Finally we have Rank [3,1,1,2,1] Par= [0,0,0,3,3]


def countComponents(n, edges):
    par = [i for i in range(n)]
    rank = [1]*n

    def find(n1):
        # find root parent
        res = n1

        while res != par[res]:
            #par[res] = par[par[res]]
            res = par[res]

        return res

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return 0

        if rank[p2] > rank[p1]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            # par changes
            par[p2] = p1
            rank[p1] += rank[p2]

        return 1

    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)

    return res


print(countComponents(5, [[0, 1], [1, 2], [3, 4]]))
