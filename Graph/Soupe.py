from abc import ABC, abstractmethod


class Piece:
    """ La piece represente une transition dans un graphe, avec une guarde et une action"""
    def __init__(self, nom: str, guard, behavior):  # Guard et action sont des lambdas
        self.nom = nom
        self.guard = guard
        self.behavior = behavior


class programConfig():
    """Nous avons notre registre EIP et x est notre variable d'exemple"""
    def __init__(self, PC = 0):
        self.PC = PC

    def copy(self):
        return programConfig(self.PC)

    def __repr__(self):
        return "ProgramConfig(PC = " + str(self.PC) + ")"

    def __eq__(self, other):
        return self.PC == other.PC

    def __hash__(self):
        return hash(self.PC)


class Soup:
    """Une soupe represente un programme, une soupe de pieces"""
    def __init__(self, start: programConfig, pieces=[]):
        """start est un program config"""
        self.start = start
        self.pieces = pieces

    def add(self, piece: Piece):
        self.pieces.append(piece)

    @property
    def roots(self):
        return self.start


class SoupSemantics:
    def __init__(self, program: Soup):
        """program est une soupe"""
        self.program = program
    
    def initial(self):
        return [self.program.start]
    
    def actions(self, config: programConfig):
        return list(filter(lambda p:p.guard(config), self.program.pieces))

    @staticmethod
    def execute(piece, config: programConfig):
        target = config.copy()
        piece.behavior(target) # Modifie target
        return [target]

