from typing import List
from ..util import *
from itertools import product

def run_prog(reg_a, reg_b, reg_c, program):
    def combo(op: int):
        match op:
            case 4: return reg_a
            case 5: return reg_b
            case 6: return reg_c
            case _: return op
    
    output = []
    pointer = 0
    prog_len = len(program)

    while pointer < prog_len:
        opcode = program[pointer]
        operand = program[pointer + 1]

        match opcode:
            case 0: #adv
                reg_a = int(reg_a/2**combo(operand))
            case 1: #bxl
                reg_b = reg_b ^ operand
            case 2: #bst
                reg_b = combo(operand) % 8
            case 3: #jnz
                if reg_a != 0:
                    pointer = operand - 2
            case 4: #bxc
                reg_b = reg_b ^ reg_c
            case 5: #out
                output.append(combo(operand) % 8)
            case 6: #bdv
                reg_b = int(reg_a/2**combo(operand))
            case 7: #cdv
                reg_c = int(reg_a/2**combo(operand))

        pointer += 2
    
    return output

def get_oct_a():
    #following only works for my input!
    #generate any a as octal number
    #list of 0 to 7 for each octal digit
    #find pattern: program from right to left / octal from left to right
    #delete digits which gives no correct output
    a1 = [3]
    a2 = [0,7]
    a3 = [7]
    a4 = [4]
    a5 = [1]
    a6 = [0]
    a7 = [3]
    a8 = [3,5]
    a9 = [1]
    a10 = [3]
    a11 = [3]
    a12 = [0,1,2,3,4,5,6,7]
    a13 = [0,1,2,3,4,5,6,7]
    a14 = [0,1,2,3,4,5,6,7]
    a15 = [0,1,2,3,4,5,6,7]
    a16 = [0,1,2,3,4,5,6,7]
    for a in product(a16, a15, a14, a13, a12, a11, a10, a9, a8, a7, a6, a5, a4, a3, a2, a1):
        yield int(f"0o{''.join(map(str,reversed(a)))}", base=8)

def execute(data: List[str], test_data: List[str]):
    def run_a(a):
        output = run_prog(a, reg_b, reg_c, program)
        if output == program: #to check patterns: start by "output[16:] == program[16:]"
            print("a:", a, "oct:", oct(a), "out:", output,"||", len(oct(a))-2, len(output))
        return output

    def join_ints(ints: list[int]):
        return ",".join(list(map(str, ints)))

    # data = test_data

    reg_a = int(data[0][12:])
    reg_b = int(data[1][12:])
    reg_c = int(data[2][12:])
    program = list(map(int, data[4][9:].split(sep=",")))

    output = run_a(reg_a)
    r1 = join_ints(output)

    reg_a_gen = get_oct_a()
    possible_as = []
    while output != program:
        reg_a = next(reg_a_gen)
        output = run_a(reg_a)
        if output == program:
            possible_as.append(reg_a)

    return r1, min(possible_as)
