from Graph.Graph_traversal import predicate_finder


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

rg = 0
def pred(c):
    if is_accepting(c[1]):
        inits = rg.neighbours(c)
        rgc = InitRG(rg, inits)

        o, k = predicate_finder(rgc, lambda cx: cx ==c)
        return o[0]
    return False