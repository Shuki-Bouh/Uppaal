from AliceEtBob.AliceEtBobSoup1 import Behaviours, programConfigAB1
from Graph.Soupe import Soup, Piece


class programConfigAB2(programConfigAB1):
    def __init__(self, alice="i", bob="i", flag_alice=False, flag_bob=False):
        super().__init__(alice, bob)
        self.flag_alice = flag_alice
        self.flag_bob = flag_bob

    def copy(self):
        return programConfigAB2(self.alice, self.bob, self.flag_alice, self.flag_bob)

    def __hash__(self):
        return hash((self.alice, self.bob, self.flag_alice, self.flag_bob))

    def __eq__(self, other):
        return (self.alice, self.bob) == (other.alice, other.bob)

    def __repr__(self):
        return f"AliceBobConfig({self.alice}, {self.bob}, {self.flag_alice}, {self.flag_bob})"


class SoupAB2(Soup):
    def __init__(self):
        alice_critical = Piece("alice_critical", lambda c: c.alice == "w" and not c.flag_bob, Behaviours.alice_action_critical)
        alice_initial = Piece("alice_initial", lambda c: c.alice == "c", Behaviours.alice_action_initial)
        alice_warning = Piece("alice_warning", lambda c: c.alice == "i", Behaviours.alice_action_warning)

        bob_critical = Piece("bob_critical", lambda c: c.bob == "w" and not c.flag_alice, Behaviours.bob_action_critical)
        bob_initial = Piece("bob_initial", lambda c: c.bob == "c", Behaviours.bob_action_initial)
        bob_warning = Piece("bob_warning", lambda c: c.bob == "i", Behaviours.bob_action_warning)
        pieces = [alice_critical, alice_warning, alice_initial, bob_critical, bob_warning, bob_initial]
        super().__init__(programConfigAB2(), pieces)