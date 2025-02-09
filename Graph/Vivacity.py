from Graph.Graph_traversal import predicate_finder, bfs_trans
from Graph.Soupe import Soup, Piece, SoupSemantics, programConfig
from Graph.RR2RG import RR2RG
from Graph.RDR import SoupDependantSemantics
from Graph.step_semantics_intersection import StepSemanticsIntersection
from AliceEtBob.AliceEtBobSoup3 import SoupAB3
from AliceEtBob.AliceEtBobSoup1 import SoupAB1
from AliceEtBob.AliceEtBobSoup2 import SoupAB2
from AliceEtBob.AliceEtBobSoup4 import SoupAB4
from Graph.decorateur import ParentTracer


class PetersonNode(programConfig):
    def __init__(self, state):
        super().__init__()
        self.state = state

    def copy(self):
        return PetersonNode(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)

    def __repr__(self):
        return "PetersonNode({})".format(self.state)


class PetersonBehavior:
    @staticmethod
    def tox(i, config: programConfig):
        config.PC += 1
        config.state = "X"

    @staticmethod
    def toy(i, config: programConfig):
        config.PC += 1
        config.state = "Y"


class Vivacite(StepSemanticsIntersection):
    """
    EXEMPLE -> q = alice.c or bob.c
    step_sync = Vivacite(
        alice_and_bob_sem,
        lambda i: i[0].alice == "c" or i[2].bob == "c"
    )
    """

    def __init__(self, semantics: SoupSemantics, q, initial):
        self.safety = False

        piece1 = Piece("X --q--> X",
                       lambda i, c: c.state == "X" and q(i),
                       PetersonBehavior.tox)

        piece2 = Piece("X --!q--> X",
                       lambda i, c: c.state == "X" and not q(i),
                       PetersonBehavior.tox)

        piece3 = Piece("X --!q--> Y",
                       lambda i, c: c.state == "X" and not q(i),
                       PetersonBehavior.toy)

        piece4 = Piece("Y --!q--> Y",
                       lambda i, c: c.state == "Y" and not q(i),
                       PetersonBehavior.toy)

        self.soup = Soup(initial, [piece1, piece2, piece3, piece4])
        self.sem = SoupDependantSemantics(self.soup)

        super().__init__(semantics, self.sem)


if __name__ == '__main__':
    # Construire le graphe avec StepSemanticsIntersection
    soupAB = (SoupAB3())
    sinter = Vivacite(SoupSemantics(soupAB), lambda i: i[2].alice == "c" or i[2].bob == "c", PetersonNode("X"))
    rr2rg = RR2RG(sinter)

    _, visited = bfs_trans(rr2rg, lambda c, o: False, [False, 0, None])
    print(f"Visited: {visited}")
    for configuration in visited:
        print(configuration)
        if configuration[1].state != "Y":
            continue

        # Il faut reconstruire TOUS les objets, pour pouvoir modifier les états initiaux...
        new_soup_spec = Soup(configuration[0], soupAB.pieces)
        new_sem = SoupSemantics(new_soup_spec)
        new_step_sync = Vivacite(
            new_sem,
            lambda i: i[2].alice == "c" or i[2].bob == "c",
            configuration[1]
        )

        target = bfs_trans(RR2RG(new_step_sync), lambda c, o, i=configuration: c == i, [False, 0, None])

        print(f"Target : {target}")
        if target[0][0]:
            print("Cycle trouvé, la vivacité n'est pas vérifiée.")
            print("Configuration trouvée : ", target)
            exit(0)

    print("Vivacité vérifiée.")