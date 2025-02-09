from abc import abstractmethod, ABC
from Graph.Profileur import profileur

class RootedDependentRelation():
    def __init__(self, program):
        """program est une soupe"""
        self.program = program

    def initial(self):
        pass

    def actions(self, i, c):
        return list(filter(lambda p: p.guard(i, c), self.program.pieces))

    def execute(self, a, i, c):
        target = c.copy()
        a.behavior(i, target)
        return [target]


class SoupDependantSemantics(RootedDependentRelation):
    def __init__(self, program):
        """program est une soupe"""
        super().__init__(program)

    @profileur.profileur
    def initial(self):
        return [self.program.start]

    @profileur.profileur
    def actions(self, i, c):
        return list(filter(lambda p: p.guard(i, c), self.program.pieces))

    @profileur.profileur
    def execute(self, a, i, c):
        target = c.copy()
        a.behavior(i, target)
        return [target]