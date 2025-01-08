from abc import abstractmethod, ABC

class RootedRelation(ABC):
    def __init__(self, root):
        self.__root = root

    @abstractmethod
    def initial(self):
        return self.__roots

    @abstractmethod
    def actions(self, c):
        pass

    @abstractmethod
    def execute(self):
        pass

