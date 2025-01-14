from abc import abstractmethod, ABC
from collections import deque

class RootedGraph(ABC):
    def __init__(self):
        return

    @abstractmethod
    @property
    def roots(self):
        return

    @abstractmethod
    @roots.setter
    def roots(self, roots):
        return

    @abstractmethod
    def neighbours(self, node):
        return

    def __eq__(self, other):
        return

    def __hash__(self):
        return 1


class DictRootedGraph(RootedGraph):
    def __init__(self, data, roots):
        super().__init__()
        self.__roots = roots
        self.__data = data

    @property
    def roots(self):
        return self.__roots

    @roots.setter
    def roots(self, r):
        self.__roots = r

    def neighbours(self, node):
        return self.__data[node] if node in self.__data else None


def pred(n, opaque):
    if n == 4:
        opaque[0] = True
        return True
    return False


def bfsTrans_v1(graph, roots):
    I = True
    k = set()
    F = deque()

    while len(F) != 0 or I:
        N = roots if I else graph[F.popleft()]
        I = False
        for n in N:
            if n not in k:
                k.add(n)
                F.append(n)
    return k


def bfsTrans_v2(graph):
    I = True
    k = set()
    F = deque()

    while len(F) != 0 or I:
        N = graph.roots if I else graph.neighbours(F.popleft())
        I = False
        for n in N:
            if n not in k:
                k.add(n)
                F.append(n)
    return k


def bfsTrans_noble(graph, pred, opaque):
    I = True
    k = set()
    F = deque()

    while len(F) != 0 or I:
        N = graph.roots if I else graph.neighbours(F.popleft())
        I = False
        for n in N:
            if n not in k:
                terminates = pred(n, opaque)
                k.add(n)
                F.append(n)
                if terminates:
                    return opaque, k
    return k


def predicate_finder(graph, predicate):
    def check_pred(n, a):
        a[1] += 1
        a[0] = predicate(n)
        if a[0]:
            a[2] = n
        return a[0]
    return bfsTrans_noble(graph, check_pred, [False, 0, None])


def breadth_first_search(graph, source):
    """
    Explore un graphe en largeur, en commençant par le sommet source.

    Args:
      graph: Le graphe.
      source: Le sommet source.

    Returns:
      Une liste des sommets du graphe, dans l'ordre dans lequel ils ont été visités.
    """

    # Initialisation
    visited = set()
    queue = [source]

    # Boucle principale
    while queue:
        u = queue.pop(0)

        # On explore les voisins de u
        if u in graph and u not in visited:
            for v in graph[u]:
                if v not in visited:
                    queue.append(v)

        visited.add(u)
    return visited


def depth_first_search(graph, source):
    """
    Explore un graphe en profondeur, en commençant par le sommet source.

    Args:
      graph: Le graphe.
      source: Le sommet source.

    Returns:
      Une liste des sommets du graphe, dans l'ordre dans lequel ils ont été visités.
    """

    # Initialisation
    visited = set()
    stack = [source]

    # Boucle principale
    while stack:
        u = stack.pop()

        # On explore les voisins de u
        if u in graph and u not in visited:
            for v in graph[u]:
                if v not in visited:
                    stack.append(v)
        visited.add(u)

    return visited


if __name__ == '__main__':


    graph = {
        1: [2, 3],
        2: [3, 4, 1],
        3: [3],
        4: []
    }
    roots = {1, 3, 1}

    graph = DictRootedGraph(graph, roots)

    print(predicate_finder(graph, lambda n: n == 4 ))