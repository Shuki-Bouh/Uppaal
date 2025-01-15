from rootedRelation import RootedRelation
from hanoi import Hanoi, HanoiNode


class HanoiRootedRelation(RootedRelation, Hanoi):

    def __init__(self, nb_disk: int):
        self.nb_disk = nb_disk
        self.nb_pilier = 3
        state_disks = [0 for _ in range(nb_disk)]
        state_piliers = {0:0}
        self.__root = [HanoiNode(state_disks, state_piliers)]

    def initial(self):
        return self.__root

    @property
    def roots(self) -> list:
        return self.__root

    @roots.setter
    def roots(self, value) -> None:
        self.__root = value

    def actions(self, node: HanoiNode) -> list:
        liste_config = []
        for disk in range(self.nb_disk):
            for pilier in range(self.nb_pilier):
                if self.check_move(node, pilier, disk):
                    liste_config.append((disk, pilier))

        return liste_config


    def execute(self, action: tuple, node: HanoiNode) -> HanoiNode:
        hanoi = Hanoi(3)

        disk, pilier = action
        new_node = hanoi.move(node, pilier, disk)
        return new_node
