from Graph.Graph_traversal import RootedGraph

class HanoiNode:
    """Cette classe représente un noeud du graphe de Hanoi.
    Un nœud est représenté par:
        - La position de chaque disque
        - Pour chaque pilier, le disque le plus haut présent sur ce pilier (None si le pilier est vide)"""

    def __init__(self, state_disks: list, state_piliers: dict, PC=0):
        """Je veux accéder au disque 2 : state_disks[2] = pilier_sur_lequel_il_se_trouve
        Je veux voir si le pilier 4 est utilisé : state_pilier[4] = disque_le_plus_haut"""
        self.state_disks = state_disks
        self.state_piliers = state_piliers
        self.PC = PC
        return

    def copy(self):
        return HanoiNode(self.state_disks, self.state_piliers, self.PC)

    def __eq__(self, other):
        """Égalité si tous les disques sont sur les mêmes piliers ..."""
        for i in range(len(self.state_disks)):
            if self.state_disks[i] != other.state_disks[i]:
                return False
        for el in self.state_piliers:
            try:
                if self.state_piliers[el] != other.state_piliers[el]:
                    return False
            except KeyError:
                return False
        return True and self.PC == other.PC

    def __hash__(self):
        return hash(tuple(self.state_disks))

    def __repr__(self):
        return str(self.state_disks)


class Hanoi(RootedGraph):
    """Cette classe représente un graphe de Hanoi."""

    def __init__(self, nb_disk: int):
        """Il est créé à partir d'un nombre de disk, un nombre de piliers et un état initial (par défaut tous les disques sont sur 0)
        Et cet état initial est un [HanoiNode]."""
        super().__init__()
        self.nb_disk = nb_disk
        self.nb_pilier = 3
        state_disks = [0 for _ in range(nb_disk)]
        state_piliers = {0:0}
        self.__root = [HanoiNode(state_disks, state_piliers)]  # Est une liste
        return

    @property
    def roots(self) -> list:
        return self.__root

    @roots.setter
    def roots(self, value) -> None:
        self.__root = value

    def check_move(self, node: HanoiNode, pilier_cible: int, disk: int) -> bool:
        """Cette fonction vérifie qu'un mouvement est possible, et renvoie un booléen"""

        state_disks = node.state_disks

        if disk >= self.nb_disk or pilier_cible >= self.nb_pilier:
            return False  # Cas qui ne doivent pas se produire

        for d in range(disk):
            if state_disks[d] == pilier_cible or state_disks[d] == state_disks[disk]:  # On regarde si un disque est au dessus ou si un disque plus petit est déjà là-bas
                return False

        return True  # Tous les cas à éviter sont vérifiés donc le mouvement est possible.

    def move(self, node: HanoiNode, pilier: int, disk: int) -> HanoiNode:
        """Cette fonction, si le mouvement a été vérifié au préalable, va effectuer le mouvement et renvoyer un HanoiNode
        qui contient le nœud suite au mouvement éffectués """

        state_disks = node.state_disks.copy()  # On prend une copie car on ne souhaite pas que le nœud courant change
                                               # d'une façon ou d'une autre (problème des valeurs mutables)
        state_piliers = node.state_piliers.copy()

        if pilier == state_disks[disk]:
            return HanoiNode(state_disks, state_piliers)

        prev_pilier = state_disks[disk]

        state_disks[disk] = pilier
        state_piliers[pilier] = disk

        for d in range(disk+1, self.nb_disk):  # Ici, on cherche le plus petit disque encore présent sur pilier d'origine
            if state_disks[d] == prev_pilier:
                state_piliers[prev_pilier] = d
                break  # On a trouvé un disque, on arrête la boucle immédiatement

        if state_piliers[prev_pilier] == disk:  # Ce cas arrive lorsqu'il n'y a plus de disque sur le pilier.
            del state_piliers[prev_pilier]  # Dans ce cas, on met la valeur de ce pilier à None (on la supprime).

        return HanoiNode(state_disks, state_piliers)  # On renvoie le HanoiNode du nouveau state_disks, state_piliers


    def neighbours(self, node: HanoiNode):
        """
        Cette fonction crée tous les mouvements possibles à partir d'un état.
        Elle utilise la fonction check_move pour verifier si un deplacement est possible
        ou non
        Renvoie une liste de tous les états voisins de node
        """

        state_piliers = node.state_piliers
        possible_states = []

        for pilier in state_piliers:
            disque = state_piliers[pilier]
            for p in range(self.nb_pilier):
                if p != pilier:  # On évite le cas où il n'y a aucun mouvement
                    if self.check_move(node, p, disque):  # On vérifie si le mouvement est possible
                        possible_states.append(self.move(node, p, disque))  # Dans ce cas, on ajoute un HanoiNode dans les mouvements possibles.
        return possible_states