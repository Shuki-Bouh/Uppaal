from Graph.step_semantics_intersection import *
from Graph.RDR import SoupDependantSemantics
from Graph.Soupe import *


class Recherche(StepSemanticsIntersection):
    """
    Propriete de safety, ça se vérifie simplement avec BFS.
    """
    def __init__(self, semantics, q, initial):
        self.safety = True

        piece1 = Piece("X --!q--> X",
                            lambda i, c: c == "X" and not q(i),
                            lambda i, c: "X")
        
        piece2 = Piece("X --q--> Y",
                            lambda i, c: c == "X" and q(i),
                            lambda i, c: "Y")

        self.soup = Soup(initial, [piece1, piece2])
        self.sem = SoupDependantSemantics(self.soup)

        super().__init__(semantics, self.sem)

class Vivacite(StepSemanticsIntersection):
    """
    EXEMPLE -> q = alice.c or bob.c
    step_sync = Vivacite(
        alice_and_bob_sem,
        lambda i: i[0].alice == "c" or i[2].bob == "c"
    )
    """
    def __init__(self, semantics, q, initial):
        self.safety = False

        piece1 = Piece("X --q--> X",
                            lambda i, c: c == "X" and q(i),
                            lambda i, c: "X")
        
        piece2 = Piece("X --!q--> X",
                            lambda i, c: c == "X" and not q(i),
                            lambda i, c: "X")
        
        piece3 = Piece("X --!q--> Y",
                            lambda i, c: c == "X" and not q(i),
                            lambda i, c: "Y")
        
        piece4 = Piece("Y --!q--> Y",
                            lambda i, c: c == "Y" and not q(i),
                            lambda i, c: "Y")

        self.soup = Soup(initial, [piece1, piece2, piece3, piece4])
        self.sem = SoupDependantSemantics(self.soup)

        super().__init__(semantics, self.sem)