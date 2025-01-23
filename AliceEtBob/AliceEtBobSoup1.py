from Graph.Soupe import *


class programConfigAB(programConfig):
    """Nous avons notre registre EIP et x est notre variable d'exemple"""
    def __init__(self, alice="i", bob="i"):
        super().__init__()
        self.PC = 1
        self.alice = alice
        self.bob = bob

    def copy(self):
        return programConfigAB(self.alice, self.bob)


class Behaviours:

    @staticmethod
    def alice_action_initial(config: programConfig):
        config.alice = "i"
        config.PC += 1

    @staticmethod
    def alice_action_warning(config: programConfig):
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
        config.bob = "w"
        config.flag_bob = True
        config.PC += 1

    @staticmethod
    def bob_action_critical(config: programConfig):
        config.bob = "c"
        config.PC += 1


alice_critical = Piece("alice_critical", lambda c: c.alice == "i", Behaviours.alice_action_critical)
alice_initial = Piece("alice_initial", lambda c: c.alice == "c", Behaviours.alice_action_initial)

bob_critical = Piece("bob_critical", lambda c: c.bob == "i", Behaviours.bob_action_critical)
bob_initial = Piece("bob_initial", lambda c: c.bob == "c", Behaviours.bob_action_initial)

initial_config = programConfigAB()
soup = Soup(initial_config, [alice_critical, alice_initial, bob_critical, bob_initial])


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
