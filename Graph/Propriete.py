from Graph.step_semantics_intersection import *
from Graph.RDR import SoupDependantSemantics
from Graph.Soupe import *

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

class Securite(StepSemanticsIntersection):
    def __init__(self, semantics, q, initial):
        self.safety = True

        piece1 = Piece("X ---!q---> X",
            lambda i, c: c.state == "X" and not q(i),
            PetersonBehavior.tox
        )
        piece2 = Piece("X ----q---> Y",
            lambda i, c: c.state == "X" and q(i),
            PetersonBehavior.toy
        )

        self.soup = Soup(initial, [piece1, piece2])
        self.sem = SoupDependantSemantics(self.soup)

        super().__init__(semantics, self.sem)

class Vivacite(StepSemanticsIntersection):

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
