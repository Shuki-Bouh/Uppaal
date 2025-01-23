from Graph.decorateur import ParentTracer
from Graph.RR2RG import RR2RG
from Graph.Graph_traversal import predicate_finder, has_deadlock
from AliceEtBob.alice_et_bob2 import AliceBob2
from AliceEtBob.alice_et_bob1 import AliceBob1

if __name__ == '__main__':

    operand = RR2RG(AliceBob2())
    graph = ParentTracer(operand)

    print(predicate_finder(graph, has_deadlock(AliceBob2())))

    operand = RR2RG(AliceBob1())
    graph = ParentTracer(operand)

    print(predicate_finder(graph, has_deadlock(AliceBob1())))