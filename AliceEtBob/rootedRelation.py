from abc import abstractmethod, ABC

class RootedRelation(ABC):

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self, node):
        pass

    @abstractmethod
    def execute(self, actions, node):
        pass

