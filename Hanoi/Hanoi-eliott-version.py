from Graph_traversal import RootedGraph
from collections import deque
import numpy as np

"""Cette version implémente l'encodage matriciel où l'état du système est représenté par une matrice.
Les lignes représentent les piliers et les colonnes les disques. La présence du disque j sur le pilier i
est donc représentée par un 1 aux coordonnées (i, j). Par conséquent, il n'y a qu'un seul 1 par colonne,
le reste de la colonne valant 0.
"""

class HanoiNode:
    def __init__(self, system_state: np.ndarray):
        self.system_state = system_state

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HanoiNode):
            return False
        return np.array_equal(self.system_state, other.system_state)

    def __repr__(self) -> str:
        return str(self.system_state)

    def __hash__(self) -> int:
        return hash(self.system_state.tobytes())


class Hanoi(RootedGraph):
    def __init__(self, nb_disk: int):
        super().__init__()
        self.nb_disk = nb_disk
        self.nb_pilier = 3
        self.system_state = np.zeros((3, self.nb_disk), dtype=int)
        self.system_state[0] = 1
        self.__root = [HanoiNode(self.system_state.copy())]

    @property
    def roots(self):
        return self.__root

    @roots.setter
    def roots(self, value):
        self.__root = value

    def check_move(self, node: HanoiNode, pilier_cible: int, disk: int) -> bool:
        system_state = node.system_state
        if disk >= self.nb_disk or pilier_cible >= self.nb_pilier:
            return False

        for j in range(disk):  # Vérifie qu'il n'y a pas de disque plus petit sur le pilier cible
            if system_state[pilier_cible, j] == 1:
                return False
        return True

    def move(self, node: HanoiNode, pilier_cible: int, disk: int) -> HanoiNode:
        system_state = node.system_state.copy()
        system_state[:, disk] = 0
        system_state[pilier_cible, disk] = 1
        return HanoiNode(system_state)

    def neighbours(self, node: HanoiNode) -> list:
        system_state = node.system_state
        possible_states = []

        for pilier_index in range(self.nb_pilier):
            # Trouver le disque au sommet du pilier
            disk_indices = np.where(system_state[pilier_index] == 1)[0]
            if disk_indices.size == 0:
                continue

            disk = disk_indices[0]
            for i in range(self.nb_pilier):
                if i != pilier_index and self.check_move(node, i, disk):
                    new_node = self.move(node, i, disk)
                    possible_states.append(new_node)
        return possible_states


def bfsTrans_up_2(graph: Hanoi, pred, opaque):
    I = True
    visited = set()
    queue = deque(graph.roots)

    while queue or I:
        nodes = graph.roots if I else graph.neighbours(queue.popleft())
        I = False
        for n in nodes:
            if n not in visited:
                terminates = pred(n, opaque)
                visited.add(n)
                queue.append(n)
                if terminates:
                    return opaque, visited
    return visited


def predicate_finder(graph: Hanoi, predicate):
    def check_pred(n, a):
        a[1] += 1
        a[0] = predicate(n)
        if a[0]:
            a[2] = n
        return a[0]

    return bfsTrans_up_2(graph, check_pred, [False, 0, None])


def predicate(node: HanoiNode) -> bool:
    # Condition: Tous les disques sont sur le dernier pilier
    return np.all(node.system_state[-1] == 1)


if __name__ == '__main__':
    graph = Hanoi(3)
    print(predicate_finder(graph, predicate))
