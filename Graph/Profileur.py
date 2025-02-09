import functools
from time import time


class Profileur:
    def __init__(self):
        self.temps_par_fonction = {}

    def reset(self):
        self.temps_par_fonction = {}

    def profileur(self, fonction):

        @functools.wraps(fonction)
        def wrapper(*args, **kwargs):
            start_time = time()  # Capture le temps de départ
            result = fonction(*args, **kwargs)
            end_time = time()  # Capture le temps de fin
            elapsed_time = end_time - start_time

            # Vérifie si la fonction appartient à une classe (dynamique)
            if args and hasattr(args[0], '__class__'):  # Si l'instance d'une classe est présente en premier argument
                class_name = args[0].__class__.__name__
            else:
                class_name = 'Global'  # Sinon, la fonction est dans le scope global

            # Stocke le temps dans l'instance
            if f"{class_name}.{fonction.__name__}" not in self.temps_par_fonction:
                self.temps_par_fonction[f"{class_name}.{fonction.__name__}"] = []

            self.temps_par_fonction[f"{class_name}.{fonction.__name__}"].append(elapsed_time)

            return result
        return wrapper

    def afficher_statistiques(self):
        """Affiche les statistiques pour chaque fonction"""
        print("\n--- Statistiques du Profileur ---")
        for nom, temps in self.temps_par_fonction.items():
            total = sum(temps)
            moyenne = total / len(temps)
            print(f"{nom}: exécuté {len(temps)} fois, temps total: {total:.6f}s, temps moyen: {moyenne:.6f}s")


# Création de l'instance du profileur
profileur = Profileur()


