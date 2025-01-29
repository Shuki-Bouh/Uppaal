from symbol import pass_stmt

from Graph import rootedRelation
from Graph.rootedRelation import RootedRelation
from Graph.Soupe import Soup, programConfig


class Buchi(Soup):
    def __init__(self):
        super().__init__()
        self.__root = None

    def initial(self) -> list:
        return [self.__root]

    def actions(self, node) -> list:


    def execute(self, actions, node) -> list:
        """À partir d'une combinaison, l'exécute et renvoie un [Node] de l'action exécutée."""
        pass


