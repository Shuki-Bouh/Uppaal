from Trash.parcours_graphe import RootedGraph


class ParentTracer(RootedGraph):
    def __init__(self, operand):
        super().__init__()
        self.parents = {}
        self.operand = operand

    @property
    def roots(self):
        rs = self.operand.roots
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

    def trace(self, final_node):
        trace_node = []
        current_node = final_node
        while current_node != self.operand.roots[0]:
            trace_node.append(current_node)
            current_node = self.parents[current_node][0]
        trace_node.append(self.operand.roots[0])
        out = str(trace_node[-1])
        for n in range(len(trace_node)-2, -1, -1):
            out = out + " -> " + str(trace_node[n])
        return out