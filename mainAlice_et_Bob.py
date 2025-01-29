from AliceEtBob.AliceEtBobSoup4 import SoupAB4
from AliceEtBob.alice_et_bob4 import AliceBob4
from Graph.decorateur import ParentTracer
from Graph.RR2RG import RR2RG
from Graph.Graph_traversal import predicate_finder, has_deadlock
from AliceEtBob.alice_et_bob2 import AliceBob2
from AliceEtBob.alice_et_bob1 import AliceBob1
from AliceEtBob.alice_et_bob3 import AliceBob3
from AliceEtBob.predicate_alice_et_bob import predicate_alicebob
from AliceEtBob.AliceEtBobSoup1 import SoupAB1
from AliceEtBob.AliceEtBobSoup2 import SoupAB2
from AliceEtBob.AliceEtBobSoup3 import SoupAB3
from Graph.Soupe import SoupSemantics

if __name__ == '__main__':

    v = 4  # ou 2 -> Permet de choisir si on veut tester la version 1 de alice et bob (sans flag), ou la version 2


    if v == 1:
        AliceBob = AliceBob1
        Soup = SoupAB1
    elif v == 2:
        AliceBob = AliceBob2
        Soup = SoupAB2
    elif v == 3:
        AliceBob = AliceBob3
        Soup = SoupAB3
    elif v == 4:
        AliceBob = AliceBob4
        Soup = SoupAB4
    else:
        raise Exception('Invalid value')

    configs = [[RR2RG(AliceBob()), "\tFonctionnement en Rootedrelation\n"],
               [RR2RG(SoupSemantics(Soup())), "\tFonctionnement en Soupsemantics\n"]] # Cela permet de tester le rootedgraph puis le soupsemantics

    for config in configs:
        operand = config[0]
        msg = config[1]

        graph = ParentTracer(operand)
        final_node = predicate_finder(graph, predicate_alicebob)
        print("___________________________________________________________")
        print(msg)
        print("Tentative de trouver la configuration Alice = C et Bob = C en cours ....")
        if final_node[0][0] == False:
            print("Alice et Bob ne se retrouvent jamais en section critique en même temps\n")
        else:
            print("Alice et Bob se retrouvent dans la section critique en même temps :")
            print(graph.trace(final_node[0][2]))
            print("")


        print("Tentative de trouver un dead lock en cours ....")

        final_node = predicate_finder(graph, has_deadlock(AliceBob()))

        if not final_node[0][0]:
            print("Pas de dead lock trouvé, gg")
        else:
            print("Dead lock en vu !")
            print(graph.trace(final_node[0][2]))

        print("___________________________________________________________")
