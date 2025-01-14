from rootedRelation import RootedRelation
from hanoi import Hanoi, HanoiNode


class HanoiRootedRelation(RootedRelation, Hanoi):

    def __init__(self, nb_disk: int):
        RootedRelation().__init__()
        Hanoi.__init__(self, nb_disk)
    
    def initial(self):
        return self.__root

    def actions(self, node: HanoiNode) -> list:
        liste_config = []
        for disk in range(self.nb_disk):
            for pilier in range(self.nb_pilier):
                if self.check_move(node, disk, pilier):
                        liste_config.append((disk, pilier))

        return liste_config


    def execute(self, actions: list, node: HanoiNode) -> HanoiNode:
        hanoi = Hanoi(3)
        for action in actions:
            disk, pilier = action
            new_node = hanoi.move(node, pilier, disk)
            return new_node
