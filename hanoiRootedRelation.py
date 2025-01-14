from rootedRelation import RootedRelation
from hanoi import Hanoi, HanoiNode


class HanoiRootedRelation(RootedRelation):

    def __init__(self, nb_disk: int):
        super().__init__()
        self.nb_disk = nb_disk
        self.nb_pilier = 3
        state_disks = [0 for _ in range(nb_disk)]
        state_piliers = {0:0}
        self.__root = [HanoiNode(state_disks, state_piliers)]

    
    def initial(self):
        return self.__root

    def actions(self, node: HanoiNode) -> list:
        liste_config = []
        for i in range(self.nb_pilier):
            for j in range(self.nb_pilier):
                if j in node.state_piliers and i in node.state_piliers :
                    if node.state_piliers[i] < node.state_piliers[j]: 
                        liste_config.append((i, j))
                elif j not in node.state_piliers and i in node.state_piliers:
                    liste_config.append((i, j))

        return liste_config


    def execute(self, actions: list, node: HanoiNode) -> HanoiNode:
        hanoi = Hanoi(3)
        for action in actions:
            disk, pilier = action
            new_node = hanoi.move(node, pilier, disk)

            return new_node
