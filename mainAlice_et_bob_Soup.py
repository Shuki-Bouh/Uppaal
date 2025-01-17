from decorateur import ParentTracer
from RR2RG import RR2RG
from Graph_traversal import predicate_finder, has_deadlock
from AliceEtBob.AliceEtBobSoup import *

if __name__ == '__main__':
    semantics = SoupSemantics(soup)
    operand = RR2RG(semantics)
    graph = ParentTracer(operand)

    print(predicate_finder(graph, has_deadlock(semantics)))