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