from rootedRelation import RootedRelation

class AliceBobNode:
    def __init__(self, a: str, b: str):
        "Vérifions si les valeurs de a et b sont correctes"
        if a not in ['i', 'w', 'c'] or b not in ['i', 'w', 'c'] :
            print("Valeure incorrete passée en paramètre")
            raise "WTFparametreError"
        self.a = a  # (i, w, ou c)
        self.b = b  # (i, w, ou c)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __hash__(self):
        return hash((self.a, self.b))

    def __repr__(self):
        return f"AliceBobNode(a={self.a}, b={self.b})"
    
class MereAliceBob(RootedRelation):
    """ Nous avons 3 automates à intégrer, Définir une classe mère est donc requis 
        afin ne pas réécrire 3 fois la même chose"""

    def __init__(self):
        super().__init__()
        self.__root = AliceBobNode(a="i", b="i")

    def initial(self):
        return self.__root

    def actions(self, node: AliceBobNode):
        pass

    def execute(self, action, node: AliceBobNode):
        """
        Exécute une action et retourne un nouvel état.
        """
        actor, new_state = action
        if actor == "alice":
            return AliceBobNode(a=new_state, b=node.b)
        elif actor == "bob":
            return AliceBobNode(a=node.a, b=new_state)

    def is_deadlock(self, node: AliceBobNode):
        """
        Vérifie si l'état actuel est un état de blocage.
        """
        return node.a == "c" and node.b == "c"


class AliceBob1(MereAliceBob):
    def __init__(self):
        super().__init__()
        self.__root = AliceBobNode(a="i", b="i")

    def actions(self, node: AliceBobNode):
        """
        Retourne les actions possibles à partir d'un état donné.
        Les actions sont des transitions possibles pour Alice ou Bob.
        """
        possible_actions = []

        # Changement d'état pour Alice
        if node.a == "i":
            possible_actions.append(("alice", "w"))
        elif node.a == "w" and node.b != "c":
            possible_actions.append(("alice", "c"))

        # Changement d'état pour Bob
        if node.b == "i":
            possible_actions.append(("bob", "w"))
        elif node.b == "w" and node.a != "c":
            possible_actions.append(("bob", "c"))

        return possible_actions


class AliceBob2(MereAliceBob):
    def __init__(self):
        super().__init__()
        # États initiaux
        self.__root = AliceBobNode(a="i", b="i")


    def actions(self, node: AliceBobNode):
        """
        Retourne les actions possibles à partir d'un état donné.
        Les actions sont des transitions possibles pour Alice ou Bob.
        """
        possible_actions = []

        # Alice peut changer son état
        if node.a == "i":
            possible_actions.append(("alice", "c"))
        elif node.a == "c":
            possible_actions.append(("alice", "i"))

        # Bob peut changer son état
        if node.b == "i":
            possible_actions.append(("bob", "c"))
        elif node.b == "c":
            possible_actions.append(("bob", "i"))

        return possible_actions


# Exemple d'utilisation
if __name__ == "__main__":
    alice_bob = AliceBob1()
    root = alice_bob.initial()

    print("État initial:", root)

    current_state = root
    while not alice_bob.is_deadlock(current_state):
        possible_actions = alice_bob.actions(current_state)
        print("Actions possibles:", possible_actions)

        if possible_actions:
            # Choisir arbitrairement la première action
            action = possible_actions[0]
            print("Exécution de l'action:", action)
            current_state = alice_bob.execute(action, current_state)
            print("Nouvel état:", current_state)
        else:
            print("Aucune action possible, arrêt.")
            break

    if alice_bob.is_deadlock(current_state):
        print("Deadlock détecté!", current_state)
