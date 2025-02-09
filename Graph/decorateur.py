from Graph.Graph_traversal import RootedGraph
from Graph.Profileur import profileur

class ParentTracer(RootedGraph):
    def __init__(self, operand):
        super().__init__()
        self.parents = {}
        self.operand = operand

    @property
    @profileur.profileur
    def roots(self):
        rs = self.operand.roots
        for r in rs:
            self.parents[r] = []
        return rs

    @profileur.profileur
    def neighbours(self, node):
        rs = self.operand.neighbours(node)
        for n in rs:
            if n not in self.parents:
                self.parents[n] = [node]
            elif self.parents[n] == []:
                self.parents[n] = [node]
        return rs

    @profileur.profileur
    def trace(self, final_node):
        """Cette fonction, une fois tout le graph parcouru, va à partir du nœud final (connaissant la root), réécrir
        le chemin de la root vers le nœud final."""
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


