class InitRG:
    def __init__(self, op, inits):
        self.op = op
        self.inits = inits

    def roots(self):
        return self.inits

    def neighbours(self, c):
        return self.op.neighbours(c)


def is_accepting(c) -> bool:
    pass


def pred(c):
    rg = InitRG(is_accepting, c)
    if is_accepting(c):
        inits =