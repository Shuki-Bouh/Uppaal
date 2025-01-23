from Graph.decorateur import ParentTracer
from Graph.RR2RG import RR2RG
from Graph.Graph_traversal import predicate_finder, has_deadlock
from AliceEtBob.alice_et_bob2 import AliceBob2
from AliceEtBob.alice_et_bob1 import AliceBob1
from AliceEtBob.predicate_alice_et_bob import predicate_alicebob

if __name__ == '__main__':

    v = 2 # ou 2

    if v == 1:
        operand = RR2RG(AliceBob1())
        graph = ParentTracer(operand)
        final_node = predicate_finder(graph, predicate_alicebob)[0]
        print("Tentative de trouver la configuration Alice = C et Bob = C\n"
              "___________________________________________________________")
        if final_node[0]:
            print(graph.trace(final_node[2]))
            print("Alice et Bob se retrouvent dans la section critique en même temps\n"
                  "___________________________________________________________")

        print("\nTentative de trouver un dead lock\n"
              "___________________________________________________________")

        final_node = predicate_finder(graph, has_deadlock(AliceBob1()))

        if final_node[0] is None:
            print("Pas de dead lock trouvé, gg \n"
                  "___________________________________________________________")

    else:
        operand = RR2RG(AliceBob2())
        graph = ParentTracer(operand)


        predicate_finder(graph, has_deadlock(AliceBob2()))

        final_node = predicate_finder(graph, predicate_alicebob)[0][2]

