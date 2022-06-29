
def deepFirstPrint(graph, source):

    stack = [source]
    while stack != []:
        current = stack.pop()
        print(current)
        stack += graph[current]


def deepFirstPrintRecursive(graph, current):

    print(current)
    for child in graph[current]:
        deepFirstPrintRecursive(graph, child)


def breadthFirstPrint(graph, source):

    stack = [source]
    while stack != []:
        current = stack.pop(0)
        print(current)
        stack += graph[current]


graph = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}


deepFirstPrintRecursive(graph, 'a')
print()
breadthFirstPrint(graph, 'a')
