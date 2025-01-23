from Hanoi.hanoi import Hanoi
from Graph.decorateur import ParentTracer
from Graph.Graph_traversal import predicate_finder
from Hanoi.predicate_hanoi import predicate_hanoi

if __name__ == '__main__':

    roots = {1, 3, 1}

    operand = Hanoi(3)
    graph = ParentTracer(operand)

    finale_node = predicate_finder(graph, predicate_hanoi)[0][2]
    print(graph.trace(finale_node))