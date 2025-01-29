from Graph.Soupe import Soup, Piece
from AliceEtBob.AliceEtBobSoup2 import programConfigAB2
from AliceEtBob.AliceEtBobSoup1 import Behaviours


class SoupAB4(Soup):
    def __init__(self):
        alice_critical = Piece("alice_critical", lambda c: c.alice == "w" and not c.flag_bob, Behaviours.alice_action_critical)
        alice_initial = Piece("alice_initial", lambda c: c.alice == "c", Behaviours.alice_action_initial)
        alice_warning = Piece("alice_warning", lambda c: c.alice == "i", Behaviours.alice_action_warning)

        bob_critical = Piece("bob_critical", lambda c: c.bob in ["w", "r"] and not c.flag_alice, Behaviours.bob_action_critical)
        bob_initial = Piece("bob_initial", lambda c: c.bob == "c", Behaviours.bob_action_initial)
        bob_R = Piece("bob_R", lambda c: c.bob == "w" and c.flag_alice, Behaviours.bob_action_r)
        bob_warning = Piece("bob_warning", lambda c: c.bob == "i", Behaviours.bob_action_warning)
        pieces = [alice_critical, alice_warning, alice_initial, bob_critical, bob_warning, bob_initial, bob_R]
        super().__init__(programConfigAB2(), pieces)