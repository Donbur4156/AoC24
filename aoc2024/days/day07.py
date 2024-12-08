from typing import List
from ..util import *
from itertools import product

test_data = ["190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20"]

def execute(data: List[str]):
    def multiply(a, b):
        return a*b
    
    def add(a, b):
        return a+b
    
    def concatenation(a, b):
        return int(str(a) + str(b))
    
    def operatorions(amount):
        return product([multiply, add], repeat=amount)
    
    def operatorions_upd(amount):
        return product([multiply, add, concatenation], repeat=amount)

    calibration_result = 0
    faulty_equations = []

    for d in data:
        value, *numbers = d.split()
        value = int(value.removesuffix(":"))
        numbers = list(map(int, numbers))
        for op_comb in operatorions(len(numbers)-1):
            val = numbers[0]
            for op, n in zip(op_comb, numbers[1:]):
                val = op(val, n)
            if val == value:
                calibration_result += value
                break
        else:
            faulty_equations.append((value, numbers))

    calibration_result_new = 0
    for value, numbers in faulty_equations:
        for op_comb in operatorions_upd(len(numbers)-1):
            val = numbers[0]
            for op, n in zip(op_comb, numbers[1:]):
                val = op(val, n)
            if val == value:
                calibration_result_new += value
                break

    return calibration_result, calibration_result + calibration_result_new
