from sys import stderr

def setup_watch_list(instance):
    watch_list = [[] for __ in range(2 * len(instance.variables))]
    for clause in instance.clauses:
        watch_list[clause[0]].append(clause)
    return watch_list

def update_watch_list(instance, watch_list, false_literal, assignment, verbose):
    while watch_list[false_literal]:
        clause = watch_list[false_literal][0]
        for alternative in clause:
            v = alternative >> 1
            a = alternative & 1
            if assignment[v] is None or assignment[v] == a ^ 1:
                watch_list[false_literal].pop(0)
                watch_list[alternative].append(clause)
                break
        else:
            if verbose:
                dump_watch_list(instance, watch_list)
                print('Current assignment: {}'.format(instance.assignment_to_string(assignment), file=stderr))
                print('Clause {} contradicted.'.format(instance.clause_to_string(clause)), file=stderr)
            return False
    return True

def dump_watch_list(instance, watch_list):
    print('Current watch list: ', file=stderr)
    for l, w in enumerate(watch_list):
        literal_string = instance.literal_to_string(l)
        clauses_string = ', '.join(instance.clause_to_string(c) for c in w)
        print('{}: {}'.format(literal_string, clauses_string), file=stderr)