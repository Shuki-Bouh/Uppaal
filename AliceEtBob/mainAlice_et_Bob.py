from Uppaal.decorateur import ParentTracer
from Uppaal.RR2RG import RR2RG
from Uppaal.Graph_traversal import predicate_finder, predicate
from alice_et_bob import AliceBob1

if __name__ == '__main__':

    operand = RR2RG(AliceBob1)
    graph = ParentTracer(operand)

    print(predicate_finder(graph, predicate))
    print(graph.parents)