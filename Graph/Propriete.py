from Graph.step_semantics_intersection import *
from Graph.RDR import SoupDependantSemantics
from Graph.Soupe import *

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

class Equite(StepSemanticsIntersection):
    """
    EXEMPLE
    -> p0: flag_alice == True
    -> q0: alice = c
    -> p1: flag_bob == False
    -> q1: bob = c
    step_sync = Equite(
        alice_and_bob_sem,
        lambda i: i[0].flag_alice,
        lambda i: i[0].alice == "c",
        lambda i: i[0].flag_bob,
        lambda i: i[0].bob == "c"
    )
    """
    def __init__(self, semantics, p0, q0, p1, q1, initial):
        self.safety = False

        piece1p0 = Piece("X --p0--> X", lambda i, c: c == "X" and p0(i), lambda i, c: "X")
        
        piece1q0 = Piece("X --q0--> X", lambda i, c: c == "X" and q0(i), lambda i, c: "X")
        
        piece1p1 = Piece("X --p1--> X", lambda i, c: c == "X" and p1(i), lambda i, c: "X")
        
        piece1q1 = Piece("X --q1--> X", lambda i, c: c == "X" and q1(i), lambda i, c: "X")
        
        piece2 = Piece("X --(p1 & !q1)--> Y", lambda i, c: c == "X" and (p1(i) and not q1(i)), lambda i, c: "Y")
        
        piece3 = Piece("X ---(p0 & !q0)--> Z", lambda i, c: c == "X" and (p0(i) and not q0(i)), lambda i, c: "Z")
        
        piece4 = Piece("Y ---!q1--> Y", lambda i, c: c == "Y" and not q1(i), lambda i, c: "Y")
        
        piece5 = Piece("Z ---!q0--> Z", lambda i, c: c == "Z" and not q0(i), lambda i, c: "Z")

        self.soup = Soup(initial, [piece1p0, piece1q0, piece1p1, piece1q1, piece2, piece3, piece4, piece5])
        self.sem = SoupDependantSemantics(self.soup)

        super().__init__(semantics, self.sem)