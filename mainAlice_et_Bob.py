from Graph.decorateur import ParentTracer
from Graph.RR2RG import RR2RG
from Graph.Graph_traversal import predicate_finder, has_deadlock
from AliceEtBob.alice_et_bob2 import AliceBob2
from AliceEtBob.alice_et_bob1 import AliceBob1
from AliceEtBob.predicate_alice_et_bob import predicate_alicebob
from AliceEtBob.AliceEtBobSoup1 import SoupAB1
from AliceEtBob.AliceEtBobSoup2 import SoupAB2
from Graph.Soupe import SoupSemantics

if __name__ == '__main__':

    v = 1  # ou 2 -> Permet de choisir si on veut tester la version 1 de alice et bob (sans flag), ou la version 2

    if v == 1:
        AliceBob = AliceBob1
        Soup = SoupAB1
    else:
        AliceBob = AliceBob2
        Soup = SoupAB2

    configs = [[RR2RG(AliceBob()), "\tFonctionnement en Rootedgraph\n"],
               [RR2RG(SoupSemantics(Soup())), "\tFonctionnement en Soupsemantics\n"]] # Cela permet de tester le rootedgraph puis le soupsemantics

    for config in configs:
        operand = config[0]
        msg = config[1]

        graph = ParentTracer(operand)
        final_node = predicate_finder(graph, predicate_alicebob)
        print("___________________________________________________________")
        print(msg)
        print("Tentative de trouver la configuration Alice = C et Bob = C en cours ....")
        if final_node[0] is None:
            print("Alice et Bob ne se retrouvent jamais en section critique en même temps\n")
        else:
            print("Alice et Bob se retrouvent dans la section critique en même temps :")
            print(graph.trace(final_node[0][2]))
            print("")


        print("Tentative de trouver un dead lock en cours ....")

        final_node = predicate_finder(graph, has_deadlock(AliceBob1()))

        if final_node[0] is None:
            print("Pas de dead lock trouvé, gg")
        else:
            print("Dead lock en vu !")

        print("___________________________________________________________")
