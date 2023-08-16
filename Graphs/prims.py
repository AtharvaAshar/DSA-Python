from queue import Queue
import sys


class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.adjMat = [[0 for _ in range(self.n_vertices)]
                       for _ in range(self.n_vertices)]

    def addEdge(self, v1, v2, wt):
        self.adjMat[v1][v2] = wt
        self.adjMat[v2][v1] = wt

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

    def __getMinVertex(self, visited, weight):
        min_vertex = -1
        for i in range(self.n_vertices):
            if visited[i] is False and (min_vertex == -1 or weight[i] < weight[min_vertex]):
                min_vertex = i
        return min_vertex

    def prims(self):
        visited = [False]*self.n_vertices
        parent = [-1]*self.n_vertices
        weightArray = [sys.maxsize for _ in range(self.n_vertices)]
        weightArray[0] = 0
        for i in range(self.n_vertices-1):
            min_vertex = self.__getMinVertex(visited, weightArray)
            visited[min_vertex] = True

            for j in range(self.n_vertices):
                if self.adjMat[min_vertex][j] > 0 and visited[j] is False:
                    if weightArray[j] > self.adjMat[min_vertex][j]:
                        weightArray[j] = self.adjMat[min_vertex][j]
                        parent[j] = min_vertex
        for i in range(1, self.n_vertices):
            if i < parent[i]:
                print(str(i) + " " +
                      str(parent[i]) + " " + str(weightArray[i]))
            else:
                print(str(parent[i]) + " " + str(i) +
                      " " + str(weightArray[i]))

    def __str__(self):
        return str(self.adjMat)


v, e = (int(ele)
        for ele in input("Enter vertices and number of edges ").split())
g = Graph(v)
for _ in range(e):
    src, dest, wt = (int(ele) for ele in input(
        "Enter src ,dest and wt of edge ").split())
    g.addEdge(src, dest, wt)

g.prims()
