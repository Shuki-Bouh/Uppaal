from Hanoi.hanoi import Hanoi
from Graph.decorateur import ParentTracer
from Graph.Graph_traversal import predicate_finder
from Hanoi.predicate_hanoi import predicate_hanoi

if __name__ == '__main__':

    roots = {1, 3, 1}

    operand = Hanoi(3)
    graph = ParentTracer(operand)

    print(predicate_finder(graph, predicate_hanoi))
    print(graph.parents)