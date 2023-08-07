from queue import Queue
class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.adjMat = [[0 for _ in range(self.n_vertices)]
                       for _ in range(self.n_vertices)]

    def addEdge(self, v1, v2):
        self.adjMat[v1][v2] = 1
        self.adjMat[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.edgePresent(v1, v2) is False:
            return
        self.adjMat[v1][v2] = 0
        self.adjMat[v2][v1] = 0

    def edgePresent(self, v1, v2):
        return True if self.adjMat[v1][v2] > 0 else False

    def __dfs_helper(self, sv, visited):

        print(sv, end=" ")
        visited[sv] = True
        for i in range(self.n_vertices):
            if self.adjMat[sv][i] > 0 and visited[i] == False:
                self.__dfs_helper(i, visited)

    def dfs(self):
        visited = [False for _ in range(self.n_vertices)]
        for i in range(self.n_vertices):
            if visited[i] is False:
                self.__dfs_helper(i, visited)

    def bfs(self):
        visited = [False for _ in range(self.n_vertices)]
        for i in range(self.n_vertices):
            if visited[i] is False:
                self.__bfs_helper(i, visited)

    def __bfs_helper(self, sv, visited):
       q = Queue()
       q.put(sv)
       visited[sv] = True
       while q.empty() is False:
           curr = q.get()
           print(curr, end=" ")
           for i in range(self.n_vertices):
            if self.adjMat[curr][i] > 0 and visited[i] == False:
                q.put(i)
                visited[i] = True

    def getPath_dfs(self, v1, v2):
        visited = [False for _ in range(self.n_vertices)]
        path = []

        def helper(v1, v2, visited):
            if self.adjMat[v1][v2] > 0:
                return [v2, v1]
            visited[v1] = True
            for i in range(self.n_vertices):
                if self.adjMat[i][v2] > 0 and visited[i] == False:
                    l = helper(i, v2, visited)
                    if l is not None:
                        l.append(v1)
                        return l

        return helper(v1, v2, visited)

    def __str__(self):
        return str(self.adjMat)


g = Graph(6)
g.addEdge(0, 3)
g.addEdge(0, 1)
g.addEdge(1, 2)
# g.addEdge(1,3)
g.addEdge(2, 3)
# g.addEdge(1,6)
# g.addEdge(1,3)
print("DFS TRAVERSAL", end=": ")
g.dfs()
print()
print("BFS TRAVERSAL", end=": ")
g.bfs()
print()

print(g.getPath_dfs(1, 3))
