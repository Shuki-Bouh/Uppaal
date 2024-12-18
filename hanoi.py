class Hanoi:

    def __init__(self, nb_disk):
        self.nb_disk = nb_disk
        self.state_disks = [0 for _ in range(nb_disk)]  # Position de chaque disque
        self.state_piliers = {}  # On place pour chaque pilier la valeur du disque le plus haut (le plus petit sur ce pilier)
        self.state_piliers[0] = 0 # Quand on commence la partie, le disque 0 est sur le pilier 0 et seul le pilier 0 est utilisé
        self.nb_pilier = 3
        return

    def move(self, pilier_cible, disk):

        if disk >= self.nb_disk or pilier_cible >= self.nb_pilier:
            return False

        for d in self.state_disks[:disk]:
            if self.state_disks[d] == pilier_cible or self.state_disks[d] == self.state_disks[disk]:
                return False

        try:
            if self.state_piliers[pilier_cible] > disk:
                self.state_piliers[pilier_cible] = disk
        except KeyError:
            self.state_piliers[pilier_cible] = disk

