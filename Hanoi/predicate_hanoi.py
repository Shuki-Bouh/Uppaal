def predicate_hanoi(node):
    state_disks = node.state_disks
    for disk in state_disks:
        if disk != 2:
            return False

    return True