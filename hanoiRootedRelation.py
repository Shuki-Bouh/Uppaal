from rootedRelation import RootedRelation

class HanoiNode:
    def __init__(self, state_disks: list, state_piliers: dict):
        self.state_disks = state_disks
        self.state_piliers = state_piliers
        return

    def __eq__(self, other):
        for i in range(len(self.state_disks)):
            if self.state_disks[i] != other.state_disks[i]:
                return False
        for el in self.state_piliers:
            try:
                if self.state_piliers[el] != other.state_piliers[el]:
                    return False
            except KeyError:
                return False
        return True

    def __hash__(self):
        return hash(tuple(self.state_disks))

    def __repr__(self):
        return str(self.state_disks)


class Hanoi(RootedRelation):

    def __init__(self, nb_disk: int):
        super().__init__()
        self.nb_disk = nb_disk
        self.nb_pilier = 3
        state_disks = [0 for _ in range(nb_disk)]
        state_piliers = {0:0}
        self.__root = [HanoiNode(state_disks, state_piliers)]

    
    def initial(self):
        return self.__root

    def actions(self, node: HanoiNode):
        liste_config = []
        for i in range(self.nb_pilier):
            for j in range(self.nb_pilier):
                if j in node.state_piliers and i in node.state_piliers :
                    if node.state_piliers[i] < node.state_piliers[j]: 
                        liste_config.append((i, j))
                elif j not in node.state_piliers and i in node.state_piliers:
                    liste_config.append((i, j))

        return liste_config


    def execute(self, actions, node):
        for action in actions:
            i, j = action
            state_disks = node.state_disks.copy()
            state_piliers = node.state_piliers.copy()
            disk = state_piliers[i]
            pilier = j
            prev_pilier = state_disks[disk]
            state_disks[disk] = pilier
            state_piliers[pilier] = disk
            for d in range(disk+1, self.nb_disk):
                if state_disks[d] == prev_pilier:
                    state_piliers[prev_pilier] = d
                    break
            if state_piliers[prev_pilier] == disk:
                del state_piliers[prev_pilier]

            return HanoiNode(state_disks, state_piliers)
