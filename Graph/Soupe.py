class Piece:
    """ La piece represente une transition dans un graphe, avec une guarde et une action"""
    def __init__(self, nom: str, guard, behavior):  # Guard et action sont des lambdas
        self.nom = nom
        self.guard = guard
        self.behavior = behavior


class programConfig():
    """Nous avons notre registre EIP et x est notre variable d'exemple"""
    def __init__(self):
        self.PC = 1


class Soup:
    """Une soupe represente un programme, une soupe de pieces"""
    def __init__(self, start: programConfig, pieces: list):
        """start est un program config"""
        self.start = start
        self.pieces = pieces

    def add(self, piece):
        self.pieces.append(piece)


class SoupSemantics:
    def __init__(self, program: Soup):
        """program est une soupe"""
        self.program = program
    
    def initial(self):
        return [self.program.start]
    
    def actions(self, c):
        return list(filter(lambda p:p.guard(c), self.program.pieces))
    
    def execute(self, piece, c):
        target = c.copy()
        piece.behavior(target) # Modifie target
        return [target]

