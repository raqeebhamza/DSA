class UnionFind:
    def __init__(self,n):
        self.parent  = [i for i in range(n+1)]
        self.rank = [1 for i in range(n+1)]
        self.count = n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def unionSet(self,x,y):
        xset ,yset= self.find(x),self.find(y)
        if xset==yset:
            return 0
        if self.rank[xset]>self.rank[yset]:
            self.parent[yset] = xset
            self.rank[xset] += self.rank[yset]
        else:
            self.parent[xset]=yset
            self.rank[yset]+=self.rank[xset]
        self.count-=1
        return 1
    def isConnected(self,x,y):
        return self.find(x)==self.find(y)
    def connectComp(self):
        return self.count