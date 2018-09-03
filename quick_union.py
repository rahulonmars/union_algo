#Quick Union algorithm

class QuickUnion():
    num = {}
    def __init__(self, N):
        for i in range(N):
            self.num[i] = i
        print ("Initial Array: ",self.num)
    
    def root(self, n):
        while not (self.num[n] == n):
            n = self.num[n]
        return n

    def connected(self, p, q):
        return self.root(p) == self.root(q)


    def union(self, p, q):
        self.num[self.root(p)] = self.root(q)
        print self.num.keys()
        print self.num.values()
        print "========"

if __name__== "__main__":
    a = QuickUnion(9)
    print(a.connected(1,2))
    print(a.connected(4,5))
    print(a.connected(4,7))
    a.union(1,2)
    a.union(4,5)
    a.union(4,7)
    print(a.connected(1,2))