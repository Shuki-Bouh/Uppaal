from abc import abstractmethod, ABC

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

    def initial(self):
        return [self.program.start]

    def actions(self, i, c):
        return list(filter(lambda p: p.guard(i, c), self.program.pieces))

    def execute(self, a, i, c):
        target = c.copy()
        a.behavior(i, target)
        return [target]