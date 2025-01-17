from Graph.RR2RG import RR2RG
from Graph.Soupe import SoupSemantics
from Graph.decorateur import ParentTracer


class Stutter:
    def __init__(self):
        pass

class StepSemanticsIntersection:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def initial(self):
        cs = []
        for lc in self.lhs.initial():
            for rc in self.rhs.initial():
                cs.append((lc, rc))
        return cs

    def actions(self, config):
        sync_actions = []
        left_config, right_config = config
        left_actions = self.lhs.actions(left_config)
        right_actions = self.rhs.actions(right_config)

        n_actions = len(left_actions)

        for left_action in left_actions:
            left_targets = self.lhs.execute(left_action, left_config)
            if len(left_targets) == 0:
                n_actions -= 1

            for left_target in left_targets:
                left_step = (left_config, left_actions, left_target)
                right_actions = self.rhs.actions(left_step, right_config)
                sync_actions.extend(map(lambda ra: (left_step, ra), right_actions))

        if n_actions == 0:
            left_step = (left_config, Stutter(), left_config)
            right_actions = self.rhs.actions(left_step, right_config)
            sync_actions.extend(map(lambda ra: (left_step, ra), right_actions))

        return sync_actions

    def execute(self, a, c):
        left_step, right_action = a
        left_configuration, right_configuration = c
        right_targets = self.rhs.execute(right_action, left_step, right_configuration)
        l_cx, l_a, left_target = left_step

        targets = map(lambda r_t: (left_target, r_t), right_targets)

        return [targets]


def nbits_3even():
    p1 = Piece("ne", lambda step, c: (sta))


if __name__ == '__main__':
    S = nbits(5)
    p, accept = nbits_3even()
    ss = SoupSemantics(S)
    sp = SoupDependantSemantics(p)

    sinter = StepSemanticsIntersection(ss, sp)

    rr2rg = RR2RG(sinter)
    pt = ParentTracer(rr2rg)

    s, n, c, k = prod_finder(pt, lambda c: accept(r_c))

    pt.get_trace(n)
