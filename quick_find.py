#quick find
#unfinished

class quickfind():
    global __id
    __id = {}
    def __init__(self, num):
        for i in num:
            __id[num] = num
    
    def connected(self, p, q):
        return __id[p] == __id[q]