from Graph.Graph_traversal import RootedGraph
from Graph.Profileur import profileur

class RR2RG(RootedGraph):

    def __init__(self, rootedRelation):
        super().__init__()
        self.op = rootedRelation

    @property
    @profileur.profileur
    def roots(self):
        return self.op.initial()

    @profileur.profileur
    def neighbours(self, node):
        possible_actions = self.op.actions(node)
        config = []
        for action in possible_actions:
            config += self.op.execute(action, node)
        return config