from hanoi import *
from collections import deque

def bfsTrans_up_2(graph, pred, opaque):
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
    return bfsTrans_up_2(graph, check_pred, [False, 0, None])

def predicate(node, opaque):
    state_disks = node[0]
    for disk in state_disks:
        if disk != 2:
            return False
        
    return True


if __name__ == '__main__':

    roots = {1, 3, 1}

    graph = Hanoi(3)

    print(predicate_finder(graph, lambda n: n == 4 ))