from abc import abstractmethod, ABC
from collections import deque

class RootedGraph(ABC):
    def __init__(self):
        return

    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def roots(self, roots):
        pass

    @abstractmethod
    def neighbours(self, node):
        pass

    def __eq__(self, other):
        return

    def __hash__(self):
        return 1



def bfsTrans(graph, pred, opaque):
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
    return bfsTrans(graph, check_pred, [False, 0, None])


def has_deadlock(sem):
    def pred(c):
        actions = sem.actions(c)
        if len(actions) == 0:
            return True
        for a in actions:
            if len(sem.execute(a, c)) > 0:
                return False
        return True
    return pred

