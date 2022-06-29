# we search for cycle in directed graph
# linear ordering of vertices in DAG
# detect cycles in topological sorting

# dfs

# start from source and stack variables and use backtracking. Rverse then ordering


def dfs(graph, vertex, path, visited):
    path.add(vertex)
    for neigh in graph[vertex]:
        if neigh in path:
            return False
        if neigh not in visited:
            visited.add(neigh)
            if not dfs(graph, neigh, path, visited):
                return False

    path.remove(vertex)
    # order.append(vertex)
    return True

# T(V,E) = O(E) + O(V)


def top_sort(graph):
    visited = set()
    path = set()
    #order = []
    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            if not dfs(graph, vertex, path, visited):
                return False

    return True
