from abc import abstractmethod, ABC

class RootedDependentRelation(ABC):

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self, i, c):
        return list(filter(lambda p: p.guard(i, c), self.program.pieces))

    @abstractmethod
    def execute(self, a, i, c):
        target = c.copy()
        a.behavior(i, target)
        return [target]


class SoupDependantSemantics(ABC):

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self, i, c):
        return list(filter(lambda p: p.guard(i, c), self.program.pieces))

    @abstractmethod
    def execute(self, a, i, c):
        target = c.copy()
        a.behavior(i, target)
        return [target]