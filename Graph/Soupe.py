class Piece:
    """ La piece represente une transition dans un graphe, avec une guarde et une action"""
    def __init__(self, nom, guard, behavior):  # Guard et action sont des lambdas
        self.nom = nom
        self.guard = guard
        self.behavior = behavior

class Soup:
    """Une soupe represente un programme, une soupe de pieces"""
    def __init__(self, start, pieces):
        """start est un program config"""
        self.start = start
        self.pieces = pieces

    def add(self, piece):
        self.pieces.append(piece)
    
class programConfig():
    """Nous avons notre registre EIP et x est notre variable d'exemple"""
    def __init__(self):
        self.PC = 1
        self.X = 0

def ap1(c):  # c est une configProgram
    c.X += 2
    c.PC += 1

p1 = Piece("p1", lambda c:c.PC+=1, ap1)

def ap2(c):
    c.X += 3
    c.PC += 1

p2 = Piece("p2", lambda c:c.PC+=1, ap2)

class SoupSemantics:
    def __init__(self, program):
        """program est une soupe"""
        self.program = program
    
    def initial(self):
        return [self.program.start]
    
    def actions(self, c):
        return list(filter(lambda p:p.guard(c), self.program.pieces))
    
    def execute(self, piece, c):
        target = c.copy()
        var = piece.behavior(target) # Modifie target, var ne sert a rien
        return [target]

