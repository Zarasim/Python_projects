# given n courses and prereq we have to find a possible course

'''
prereq= [[0,1],[0,2],[1,3],[1,4],[3,4]]

0  - 1 - 3
|    |  /
2     4

Use deep first search

Visitedset allows to detect cycles

'''

# preMap 0 [1,2]
#        1 [3,4]
#        2  []
#        3  [4]
#        4  []


from calendar import c

from torch import prepare_multiprocessing_environment


def canFinish(numCourses, prereq):
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in prereq:
        preMap[crs].append(pre)

    visitedset = set()

    def dfs(crs):
        if crs in visitedset:
            return False
        if preMap[crs] == []:
            return True

        visitedset.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False

        visitedset.remove(crs)
        preMap[crs] = []
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False

    return True
