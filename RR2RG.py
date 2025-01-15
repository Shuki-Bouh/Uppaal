from parcours_graphe import RootedGraph

class RR2RG(RootedGraph):

    def __init__(self, rootedRelation):
        super().__init__()
        self.op = rootedRelation

    @property
    def roots(self):
        return self.op.initial()

    def neighbours(self, node):
        possible_actions = self.op.actions(node)
        config = []
        for action in possible_actions:
            config.append(self.op.execute(action, node))
        return config