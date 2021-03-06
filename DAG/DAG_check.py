# Single Source Shortest Path problem is solved on O(V+E). There is a topological order via topsort and processed sequentially
# It can deal with negative weights
# We can choose an arbitrary order and associate infinity
# Longest path is NP-hard on general graphs, but on DAG is solvable in O(V + E). Multiply all edge values by -1, take shortest path and remultiply by -1.


# Python program to find single source shortest paths
# for Directed Acyclic Graphs Complexity :OV(V+E)
from collections import defaultdict

# Graph is represented using adjacency list. Every
# node of adjacency list contains vertex number of
# the vertex to which edge connects. It also contains
# weight of the edge


class Graph:
    def __init__(self, vertices):

        self.V = vertices  # No. of vertices

        # dictionary containing adjacency List
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    # A recursive function used by shortestPath
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                if visited[node] == False:
                    self.topologicalSortUtil(node, visited, stack)

        # Push current vertex to stack which stores topological sort
        stack.append(v)

    ''' The function to find shortest paths from given vertex.
        It uses recursive topologicalSortUtil() to get topological
        sorting of given graph.'''

    def shortestPath(self, s):

        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from source vertices
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(s, visited, stack)

        # Initialize distances to all vertices as infinite and
        # distance to source as 0
        dist = [float("Inf")] * (self.V)
        dist[s] = 0

        # Process vertices in topological order
        while stack:

            # Get the next vertex from topological order
            i = stack.pop()

            # Update distances of all adjacent vertices
            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight

        # Print the calculated shortest distances
        for i in range(self.V):
            print(("%d" % dist[i]) if dist[i] !=
                  float("Inf") else "Inf", end=" ")
