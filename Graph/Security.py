class Securite(composition.StepSyncComposition):
    """
    Propriete de safety, ça se vérifie simplement avec BFS.
    """
    def __init__(self, semantics, q, initial):
        self.safety = True

        piece1 = soup.Piece("X ---!q---> X",
            lambda i, c: c == "X" and not q(i),
            lambda i, c: "X"
        )
        piece2 = soup.Piece("X ----q---> Y",
            lambda i, c: c == "X" and q(i),
            lambda i, c: "Y"
        )

        self.soup = soup.SoupSpec([initial], [piece1, piece2])
        self.sem = composition.DependentSoupSemantics(self.soup)

        super().__init__(semantics, self.sem)
