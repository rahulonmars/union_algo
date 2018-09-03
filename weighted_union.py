from quick_union import QuickUnion

class WeightedUnion(QuickUnion):
    sz = {} # to count number of elements in a tree
    def count(self, i):
        ''' count number of elements in the tree rooted at 'root' '''
        root_i = self.root(i)
        traverse = [root_i]
        #print "Traverse: ",traverse
        while traverse:
            for child in traverse:
                self.sz[child] = 0
                #print "Child: ",child
                traverse.remove(child)
                for number in range(len(self.num)):
                    #print "Number :",number
                    if child == self.root(number) and child != number:
                        #print "Incrementing"
                        self.sz[child] += 1
                        #traverse.append(number)
                    else:
                        pass
        print "Number of elements in {0} tree: {1}".format(i,self.sz[child])
        return self.sz[child]
    
    def union(self, p, q):
        print "Method in Weighted Union"
        # q_size = self.sz.get(self.root(q),0)
        # p_size = self.sz.get(self.root(p),0)

        q_size = self.count(q)
        p_size = self.count(p)

        if self.count(p) < self.count(q):
            self.num[self.root(p)] = self.root(q)
            self.sz[self.root(q)] += p_size

            print "sz: ",self.sz
            print self.num.keys()
            print self.num.values()
        else:
            self.num[self.root(q)] = self.root(p)
            self.sz[self.root(p)] += q_size
            
            print "sz: ",self.sz
            print self.num.keys()
            print self.num.values()

a = WeightedUnion(10)
print "Root of 3:",a.root(3)
print "Root of 4:",a.root(4)
a.union(3,4)
a.union(4,9)
a.union(8,0)
a.union(2,3)
a.union(5,6)
a.union(5,9)
a.union(7,3)
a.union(4,8)
a.union(6,1)
print(a.count(3))