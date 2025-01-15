from parcours_graphe import RootedGraph


class ParentTracer(RootedGraph):
    def __init__(self, operand):
        self.parents = {}
        self.operand = operand

    @property
    def roots(self):
        rs = self.operand.roots  # Hanoi node
        for r in rs:
            self.parents[r] = []
        return rs

    def neighbours(self, v):
        rs = self.operand.neighbours(v)
        for n in rs:
            if n not in self.parents:
                self.parents[n] = [v]
            elif self.parents[n] == []:
                self.parents[n] = [v]
        return rs