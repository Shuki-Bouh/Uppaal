from decorateur import ParentTracer
from RR2RG import RR2RG
from Graph_traversal import predicate_finder, predicate
from hanoiRootedRelation import Hanoi

if __name__ == '__main__':

    roots = {1, 3, 1}

    operand = RR2RG(Hanoi(3))
    graph = ParentTracer(operand)

    print(predicate_finder(graph, predicate))
    print(graph.parents)