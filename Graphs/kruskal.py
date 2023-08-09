class Edge:
    def __init__(self,src,dest,wt) -> None:
        self.src=src
        self.dest=dest
        self.wt=wt
def getParent(v,parent):
    if (v==parent[v]):
        return v
    return getParent(parent[v],parent)
def kruskal(edges,v):
    parent=[n for n in range(v)]
    edges=sorted(edges,key=lambda x:x.wt)
    c=0
    output=[]
    i=0
    while c<v-1:
        currEdge=edges[i]
        srcParent=getParent(currEdge.src,parent)
        destParent=getParent(currEdge.dest,parent)
        if srcParent!=destParent:
            output.append(currEdge) 
            parent[srcParent]=destParent
            c+=1
        i+=1
    return output



v,e=(int(ele) for ele in input("Enter vertices and number of edges ").split())
edges=[]
for _ in range(e):
    src,dest,wt=(int(ele) for ele in input("Enter src ,dest and wt of edge ").split())
    edge=Edge(src,dest,wt)
    edges.append(edge)

output=kruskal(edges,v)
print()
cost=0
for e in output:
    print(e.src,e.dest,e.wt)
    cost+=e.wt
print(cost)
