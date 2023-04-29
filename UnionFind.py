class UnionFind:
    def __init__(self,n):
        self.parent  = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.count = n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def unionSet(self,x,y):
        xset ,yset= self.find(x),self.find(y)
        if self.rank[xset]>self.rank[yset]:
            self.parent[xset]=yset
        elif self.rank[xset] < self.rank[yset]:
            self.parent[yset]=xset
        else:
            self.parent[yset]=xset
            self.rank[xset]
