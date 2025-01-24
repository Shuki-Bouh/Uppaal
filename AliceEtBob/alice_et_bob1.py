from Graph.rootedRelation import RootedRelation

class AliceBobNode1:
    def __init__(self, alice: str, bob: str):
        """Lors de l'initialisation d'un node, on vérifie que les paramètres passés correspondent à quelque chose"""
        if alice not in ['i', 'w', 'c'] or bob not in ['i', 'w', 'c']:
            print("Valeure incorrete passée en paramètre")
            raise "WTFparametreError"
        self.alice = alice  # (i, w, ou c)
        self.bob = bob  # (i, w, ou c)

    def __eq__(self, other):
        return self.alice == other.alice and self.bob == other.bob

    def __hash__(self):
        return hash((self.alice, self.bob))

    def __repr__(self):
        return f"AliceBobNode(a={self.alice}, b={self.bob})"


class AliceBob1(RootedRelation):
    def __init__(self):
        super().__init__()
        # États initiaux
        self.__root = [AliceBobNode1(alice="i", bob="i")]

    def initial(self):
        return self.__root

    def actions(self, node: AliceBobNode1):
        """
        Retourne les actions possibles à partir d'un état donné.
        Les actions sont des transitions possibles pour Alice ou Bob.
        """
        possible_actions = []

        # Alice peut changer son état
        if node.alice == "i" and node.bob == "i":
            possible_actions.append(("alice", "c"))
        elif node.alice == "c":
            possible_actions.append(("alice", "i"))

        # Bob peut changer son état
        if node.bob == "i" and node.alice == "i":
            possible_actions.append(("bob", "c"))
        elif node.bob == "c":
            possible_actions.append(("bob", "i"))

        return possible_actions

    def execute(self, action, node: AliceBobNode1):
        """
        Exécute une action et retourne un nouvel état.
        """
        actor, new_state = action
        if actor == "alice":
            return [AliceBobNode1(alice=new_state, bob=node.bob)]
        elif actor == "bob":
            return [AliceBobNode1(alice=node.alice, bob=new_state)]

    def is_deadlock(self, node: AliceBobNode1):
        """
        Vérifie si l'état actuel est un état de blocage.
        """
        return len(self.actions(node)) == 0
