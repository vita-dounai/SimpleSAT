#!/usr/bin/env python3

import sys

from sat_instance import SATInstance
from sat.watch_list import setup_watch_list
from sat.recursive_solver import solve

def main(input_file):
    instance = SATInstance.from_file(input_file)
    print('---------------------------')
    print('Clauses:')
    for clause in instance.clauses:
        print(instance.clause_to_string(clause))
    watch_list = setup_watch_list(instance)
    assignment = [None] * len(instance.variables)
    count = 1
    print('---------------------------')
    print('Solutions:')
    for solution in solve(instance, watch_list, assignment, 0, False):
        assignment_string = instance.assignment_to_string(solution)
        print('#{}: {}'.format(count, assignment_string))
        count += 1

main(sys.argv[1])
