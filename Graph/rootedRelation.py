from abc import abstractmethod, ABC

class RootedRelation(ABC):

    @abstractmethod
    def initial(self) -> list:
        """Renvoie les racines du graph : [Node]"""
        pass

    @abstractmethod
    def actions(self, node) -> list:
        """Renvoie toutes les combinaisons possibles à partir d'un Node"""
        pass

    @abstractmethod
    def execute(self, actions, node) -> list:
        """À partir d'une combinaison, l'exécute et renvoie un [Node] de l'action exécutée."""
        pass

