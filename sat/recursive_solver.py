from sys import stderr

from .watch_list import update_watch_list

def solve(instance, watch_list, assignment, d, verbose):
    if d == len(instance.variables):
        yield assignment
        return
    
    for a in [0, 1]:
        if verbose:
            print('Trying {}={}'.format(instance.variables[d], a), file=stderr)
        assignment[d] = a
        if update_watch_list(instance, watch_list, (d << 1) | a, assignment, verbose):
            for a in solve(instance, watch_list, assignment, d + 1, verbose):
                yield a
    
    assignment[d] = None