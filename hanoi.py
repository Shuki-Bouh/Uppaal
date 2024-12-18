from parcours_graphe import RootedGraph

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




class Hanoi(RootedGraph):

    def __init__(self, nb_disk: int):
        super().__init__()
        self.nb_disk = nb_disk
        self.nb_pilier = 3
        self.__root = [0 for _ in range(nb_disk)]
        return

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        self.__root = value

    def check_move(self, node: HanoiNode, pilier_cible: int, disk: int):

        state_disks = node.state_disks # node = ([list_state_disks], {dict_state_pilier})

        if disk >= self.nb_disk or pilier_cible >= self.nb_pilier:
            return False  # Cas qui ne doivent pas se produire

        for d in state_disks[:disk]:
            if state_disks[d] == pilier_cible or state_disks[d] == state_disks[disk]:  # On regarde si un disque est au dessus ou si un disque plus petit est déjà là-bas
                return False

        return True

    def move(self, node: HanoiNode, pilier: int, disk: int):
        state_disks = node.state_disks.copy()
        state_piliers = node.state_piliers.copy()

        prev_pilier = state_disks[disk]

        state_disks[disk] = pilier
        state_piliers[pilier] = disk

        for d in state_disks[disk:]:
            if state_disks[d] == prev_pilier:
                state_piliers[prev_pilier] = d
                break

        if state_piliers[prev_pilier] == disk:
            del state_piliers[prev_pilier]

        return HanoiNode(state_disks, state_piliers)


    def neighbours(self, node: HanoiNode):
        """
        Cette fonction créé tous les mouvement possibles à partir d'un état
        Elle utilise la fonction check_move pour verifier si un deplacement est possible
        ou non
        Renvoie une liste de tous les états voisins de node
        """
        state_piliers = node.state_piliers
        possible_states = []

        for pilier in state_piliers:
            disque = state_piliers[pilier]
            for p in range(self.nb_pilier):
                if p != pilier:
                    if self.check_move(node, p, disque):
                        possible_states.append(self.move(node, p, disque))
        return possible_states