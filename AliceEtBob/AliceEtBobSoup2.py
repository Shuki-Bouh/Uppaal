from AliceEtBobSoup1 import *


class programConfigAB2(programConfigAB):
    def __init__(self, alice="i", bob="i", flag_alice=False, flag_bob=False):
        super().__init__(alice, bob)
        self.flag_alice = flag_alice
        self.flag_bob = flag_bob