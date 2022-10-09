import sys

class Edge:
    def __init__(self, f_, t_, i_):
        self.m_nFrom = f_
        self.m_nTo = t_
        self.m_sInput = i_
    def print(self):
        print("%d,%d,%s" % (self.m_nFrom, self.m_nTo, self.m_sInput))

class Graph:
    def __init__(self, fp_=0):
        self.m_lEdges = []
        if(fp_ != 0):
            for line in fp_:
                elem = line[0:-1].split(',')
                self.m_lEdges.append(Edge(int(elem[0]), int(elem[1]), elem[2]))
    def getEClosureS(self, s_):
        r = set()
        r.add(s_)
        edges = self.m_lEdges
        for i in range(len(edges)):
            for j in range(i, len(edges)):
                for p in list(r):
                    if p == edges[j].m_nFrom and edges[j].m_sInput == '':
                        r.add(edges[j].m_nTo)
        return r
    def getEClosureT(self, t_):
        r = set()
        for i in t_:
            for p in self.getEClosureS(i):
                r.add(p)
        return r
    def getMove(self, t_, a_):
        r = set()
        edges = self.m_lEdges
        for edge in edges:
            for frm in t_:
                if frm == edge.m_nFrom and edge.m_sInput == a_:
                    r.add(edge.m_nTo)
        return r
    def print(self):
        for e in self.m_lEdges:
            e.print()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: python %s <input file>" % sys.argv[0])
    fp = open(sys.argv[1], "r")
    NFA = Graph(fp)

    print(NFA.getEClosureS(0))
    print(NFA.getMove({0, 1, 2, 4, 7}, 'a'))
    print(NFA.getEClosureT({3, 8}))
    print(NFA.getMove({0, 1, 2, 4, 7}, 'b'))
    print(NFA.getEClosureT({5}))
