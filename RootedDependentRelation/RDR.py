from abc import abstractmethod, ABC

class RootedDependentRelation(ABC):

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self, i, c):
        pass

    @abstractmethod
    def execute(self, a, i, c):
        pass
