#!/usr/bin/env python
from collections import defaultdict
from sys import stdin


def read_code(inp):
    for line in inp.readlines():
        yield line.strip().split(' ')


def run_code(code):
    stack = []
    values = defaultdict(int)
    position = 0
    while position < len(code):
        arg, *rest = code[position]
        if arg.startswith('x'):
            if rest:
                assignment_operator, *arguments = rest
                if assignment_operator == '=':
                    values[arg] = int(arguments[0])
                elif assignment_operator == '-=':
                    values[arg] -= int(arguments[0])
                elif assignment_operator == '+=':
                    values[arg] += int(arguments[0])
                else:
                    raise SyntaxError()
            else:
                print(values[arg])
        elif arg == 'WHILE':
            stack.append((position, rest[0]))
        elif arg == 'END':
            stored_position, name = stack.pop()
            if values[name]:
                position = stored_position
                stack.append((stored_position, name))
        else:
            raise SyntaxError("Unknown instr. {}".format(arg))
        position += 1


if __name__ == "__main__":
    c = tuple(read_code(stdin))
    run_code(c)
