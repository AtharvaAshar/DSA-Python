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

    

    def __str__(self):
        return str(self.adjMat)
    
    def isConnected(self,sv):
        visited = [False for _ in range(self.n_vertices)]
        def helper(v1,v2,visited):
            visited[v1] = True
            for i in range(self.n_vertices):
                if self.adjMat[v1][i] > 0 and visited[i] == False:
                    helper(i, v2, visited)
        for i in range(self.n_vertices):
            helper(sv,i,visited)
        if False in visited:
            return False
        else:
            return True
g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 4)
print("DFS TRAVERSAL", end=": ")
g.dfs()
print()
print("BFS TRAVERSAL", end=": ")
g.bfs()
print()
print(g.isConnected(0))
