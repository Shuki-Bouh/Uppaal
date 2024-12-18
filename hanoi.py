from parcours_graphe import RootedGraph

class Hanoi(RootedGraph):

    def __init__(self, nb_disk):
        self.nb_disk = nb_disk
        self.nb_pilier = 3
        return

    def check_move(self, node, pilier_cible, disk):

        state_disks, state_piliers = node  # node = ([list_state_disks], {dict_state_pilier})

        if disk >= self.nb_disk or pilier_cible >= self.nb_pilier:
            return False  # Cas qui ne doivent pas se produire

        for d in state_disks[:disk]:
            if state_disks[d] == pilier_cible or state_disks[d] == state_disks[disk]:  # On regarde si un disque est au dessus ou si un disque plus petit est déjà là-bas
                return False

        return True


    def neighbours(self, node):
        """
        Cette fonction créé tous les mouvement possibles à partir d'un état
        Elle utilise la fonction check_move pour verifier si un deplacement est possible
        ou non
        Renvoie une liste de tous les états voisins de node
        """
        state_disque, state_pilier = node
        for pilier in state_pilier:
            disque = state_pilier[pilier]
            for j in range(self.nb_pilier):
                if j !=pilier:
                    self.check_move(node, j, disque)