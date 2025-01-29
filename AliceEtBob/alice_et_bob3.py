from Graph.rootedRelation import RootedRelation
from AliceEtBob.alice_et_bob2 import AliceBobNode2


class AliceBob3(RootedRelation):
    def __init__(self):
        super().__init__()
        self.__root = [AliceBobNode2(alice="i", bob="i", flag_alice=False, flag_bob=False),]

    def initial(self):
        return self.__root

    def actions(self, node: AliceBobNode2):
        """
        Retourne les actions possibles à partir d'un état donné.
        Les actions sont des transitions possibles pour Alice ou Bob.
        """
        possible_actions = []

        # Changement d'état pour Alice
        if node.alice == "i":
            possible_actions.append(("alice", "w", True))
        elif node.alice == "w" and not node.flag_bob:  # flag_bob == False, est abaissé
            possible_actions.append(("alice", "c", True))
        elif node.alice == "c":
            possible_actions.append(("alice", "i", False))

        # Changement d'état pour Bob
        if node.bob == "i":
            possible_actions.append(("bob", "w", True))
        elif node.bob == "w" and not node.flag_alice:
            possible_actions.append(("bob", "c", True))
        elif node.bob == "c":
            possible_actions.append(("bob", "i", False))
        elif node.bob == "w" and node.flag_alice:  # C'est le nouveau chemin (cela peut se factoriser ...)
            possible_actions.append(("bob", "i", False))
        return possible_actions

    def execute(self, action, node: AliceBobNode2):
        actor, new_state, new_flag = action
        if actor == "alice":
            return [AliceBobNode2(alice=new_state, bob=node.bob, flag_alice=new_flag, flag_bob=node.flag_bob)]
        elif actor == "bob":
            return [AliceBobNode2(alice=node.alice, bob=new_state, flag_alice=node.flag_alice, flag_bob=new_flag)]


