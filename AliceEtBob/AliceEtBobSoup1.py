from Graph.Soupe import *


class programConfigAB1(programConfig):
    def __init__(self, alice="i", bob="i"):
        super().__init__()
        self.PC = 1
        self.alice = alice
        self.bob = bob

    def copy(self) -> "programConfigAB1":
        return programConfigAB1(self.alice, self.bob)

    def __repr__(self):
        return f"AliceBobConfig(a={self.alice}, b={self.bob})"

    def __hash__(self):
        return hash((self.alice, self.bob))

    def __eq__(self, other):
        return (self.alice, self.bob) == (other.alice, other.bob)


class Behaviours:
    """Cette classe regroupe les différents behaviours existants pour Alice et Bob (regroupe la v1 et la v2)"""

    @staticmethod
    def alice_action_initial(config: programConfig) -> None:
        config.alice = "i"
        config.PC += 1

    @staticmethod
    def alice_action_warning(config: programConfig):
        """Uniquement pour la v2"""
        config.alice = "w"
        config.flag_alice = True
        config.PC += 1

    @staticmethod
    def alice_action_critical(config: programConfig):
        config.alice = "c"
        config.PC += 1

    @staticmethod
    def bob_action_initial(config: programConfig):
        config.bob = "i"
        config.PC += 1

    @staticmethod
    def bob_action_warning(config: programConfig):
        """Uniquement pour la v2"""
        config.bob = "w"
        config.flag_bob = True
        config.PC += 1

    @staticmethod
    def bob_action_critical(config: programConfig):
        config.bob = "c"
        config.PC += 1


class SoupAB1(Soup):
    """Permet de préparer la soup plus rapidement que si c'était fait dans le main"""
    def __init__(self):
        alice_critical = Piece("alice_critical", lambda c: c.alice == "i", Behaviours.alice_action_critical)
        alice_initial = Piece("alice_initial", lambda c: c.alice == "c", Behaviours.alice_action_initial)

        bob_critical = Piece("bob_critical", lambda c: c.bob == "i", Behaviours.bob_action_critical)
        bob_initial = Piece("bob_initial", lambda c: c.bob == "c", Behaviours.bob_action_initial)
        pieces = [alice_critical, alice_initial, bob_critical, bob_initial]
        super().__init__(programConfigAB1(), pieces)


