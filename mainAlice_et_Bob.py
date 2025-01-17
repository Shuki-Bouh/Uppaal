from Graph.decorateur import ParentTracer
from Graph.RR2RG import RR2RG
from Graph.Graph_traversal import predicate_finder, has_deadlock
from AliceEtBob.alice_et_bob import AliceBob1

if __name__ == '__main__':

    operand = RR2RG(AliceBob1())
    graph = ParentTracer(operand)

    print(predicate_finder(graph, has_deadlock(AliceBob1())))