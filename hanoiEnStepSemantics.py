from Graph.Soupe import SoupSemantics, Piece, Soup, programConfig
from Graph.RDR import SoupDependantSemantics
from Graph.step_semantics_intersection import StepSemanticsIntersection
from Hanoi.hanoi import HanoiNode
from Graph.Graph_traversal import predicate_finder
from Graph.decorateur import ParentTracer
from Graph.RR2RG import RR2RG

def nbits(nbbits):
    soup = Soup(programConfig())
    def flip(i):
        def occ(c):
            c.PC = c.PC^(1 << i)
        return occ
    for i in range(nbbits):
        soup.add(Piece(f'{i}', lambda c : True, flip(i)))
    return soup


def nbits_3even():
    p1 = Piece("ne", lambda step, c: step[0].PC % 2 == 0, incr)
    p2 = Piece("even", lambda step, c: step[0].PC % 2 == 1, lambda step, c: None)
    return Soup(programConfig(), [p1, p2]), lambda c: c[1].PC == 3

def hanoi_moves(nb_disks=3, nb_piliers=3):
    soup = Soup(HanoiNode([0,0,0], {0:0}))

    def move_piece(disk, target_pilier):
        def action(step, c):
            node = step[0]
            if node.check_move(node, target_pilier, disk):
                step[0] = node.move(node, target_pilier, disk)
        return action

    for disk in range(nb_disks):
        for pilier in range(nb_piliers):
            soup.add(Piece(f"disk {disk} ---> {pilier}",
                           lambda step, c, d=disk, p=pilier: step[0].check_move(step[0], p, d),
                           move_piece(disk, pilier)))

    return soup

def hanoi_even():
    return Soup(HanoiNode([0,0,0],{0:0}), []), lambda c: c[0].state_disks[0] == 2 and c[0].state_disks[1] == 2 and c[0].state_disks[2] == 2


if __name__ == '__main__':

    program, accept = hanoi_even()
    soup_semantics = SoupSemantics(hanoi_moves())
    soup_dependant_semantics = SoupDependantSemantics(program)

    sinter = StepSemanticsIntersection(soup_semantics, soup_dependant_semantics)

    rr2rg = RR2RG(sinter)
    graph = ParentTracer(rr2rg)

    final_node = predicate_finder(graph, accept)
    if final_node[0][0]:
        print(graph.trace(final_node[0][2]))
    else:
        print("Predicate not found")
        print(final_node[1])