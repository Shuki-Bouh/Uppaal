from Graph.decorateur import ParentTracer
from Graph.RR2RG import RR2RG
from Graph.Graph_traversal import predicate_finder
from Hanoi.predicate_hanoi import predicate_hanoi
from Hanoi.hanoiRootedRelation import HanoiRootedRelation

if __name__ == '__main__':
    operand = RR2RG(HanoiRootedRelation(3))
    graph = ParentTracer(operand)

    print(predicate_finder(graph, predicate_hanoi))