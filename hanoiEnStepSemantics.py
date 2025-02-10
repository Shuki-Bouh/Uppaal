def nbits(nbbits):
    soup = Soup(programConfig())
    def flip (i):
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