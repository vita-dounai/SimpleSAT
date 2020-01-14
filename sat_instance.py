class SATInstance(object):
    def __init__(self):
        self.variables = []
        self.variables_table = dict()
        self.clauses = []

    def parse_and_add_clause(self, line):
        clause = []
        for literal in line.split():
            negated = 1 if literal.startswith('~') else 0
            variable = literal[negated:]
            if variable not in self.variables_table:
                self.variables_table[variable] = len(self.variables)
                self.variables.append(variable)
            encoded_literal = self.variables_table[variable] << 1 | negated
            clause.append(encoded_literal)
        self.clauses.append(clause)

    @classmethod
    def from_file(cls, file):
        instance = cls()
        for line in open(file):
            line = line.strip()
            if len(line) > 0 and not line.startswith('#'):
                instance.parse_and_add_clause(line)
        return instance

    def literal_to_string(self, literal):
        str = '~' if literal & 1 else ''
        return str + self.variables[literal >> 1]

    def clause_to_string(self, clause):
        literals = []
        for literal in clause:
            literals.append(self.literal_to_string(literal))
        return ' '.join(literals)

    def assignment_to_string(self, assigement, brief=False, starting_with=''):
        literals = []
        for a, v in ((a, v) for a, v in zip(assigement, self.variables) if v.startswith(starting_with)):
            if a == 0 and not brief:
                literals.append('~' + v)
            elif a:
                literals.append(v)
        return ' '.join(literals)