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
    def __init__(self, a="i", b="i"):
        self.PC = 1
        self.a = a
        self.b = b

    def copy(self):
        return programConfig(self.a, self.b)

def alice_action_write(c):
    c.alice = "w"
    c.PC += 1

def alice_action_commit(c):
    c.alice = "c"
    c.PC += 1

def alice_action_idle(c):
    c.alice = "i"
    c.PC += 1

def bob_action_write(c):
    c.bob = "w"
    c.PC += 1

def bob_action_commit(c):
    c.bob = "c"
    c.PC += 1

def bob_action_idle(c):
    c.bob = "i"
    c.PC += 1

alice_write = Piece("alice_write", lambda c: c.alice == "i", alice_action_write)
alice_commit = Piece("alice_commit", lambda c: c.alice == "w", alice_action_commit)
alice_idle = Piece("alice_idle", lambda c: c.alice == "c", alice_action_idle)

bob_write = Piece("bob_write", lambda c: c.bob == "i", bob_action_write)
bob_commit = Piece("bob_commit", lambda c: c.bob == "w", bob_action_commit)
bob_idle = Piece("bob_idle", lambda c: c.bob == "c", bob_action_idle)

initial_config = programConfig()
soup = Soup(initial_config, [alice_write, alice_commit, alice_idle, bob_write, bob_commit, bob_idle])

class SoupSemantics:
    def __init__(self, program):
        """program est une soupe"""
        self.program = program

    def initial(self):
        return [self.program.start]

    def actions(self, c):
        return list(filter(lambda p: p.guard(c), self.program.pieces))

    def execute(self, piece, c):
        target = c.copy()
        piece.behavior(target)  # Modifie target
        return [target]


if __name__ == "__main__":
    semantics = SoupSemantics(soup)
    current_states = semantics.initial()

    print("État initial:", current_states[0].__dict__)

    while current_states:
        next_states = []
        deadlock_detected = True  # Assume deadlock until proven otherwise
        
        for state in current_states:
            actions = semantics.actions(state)
            print(f"Actions possibles pour {state.__dict__}: {[a.nom for a in actions]}")
            
            if actions:  # If any action is possible, no deadlock in this state
                deadlock_detected = False
                for action in actions:
                    next_states.extend(semantics.execute(action, state))

        if deadlock_detected:
            print("Deadlock détecté. Aucun état suivant possible.")
            break

        current_states = next_states

        if not current_states:
            print("Aucun état suivant, arrêt.")
            break

        for state in current_states:
            print("Nouvel état:", state.__dict__)
