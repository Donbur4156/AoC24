from typing import List
from ..util import *
import re

test_data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

def execute(data: List[str]):
    def find_xmas(line: str):
        return len(re.findall(r"XMAS", line)) + len(re.findall(r"SAMX", line))
    len_data = len(data)
    amount_xmas = 0
    #horizontal
    amount_xmas += sum(find_xmas(d) for d in data)
    #vertikal
    amount_xmas += sum(find_xmas("".join([l[i] for l in data])) for i in range(len_data))
    #diagonal l>r
    for i in range(-len_data, len_data):
        f = [data[j][i+j] for j in range(max(-i,0), min(len_data-i, len_data))]
        amount_xmas += find_xmas("".join(f))
    #diagonal r>l
    for i in range(len_data*2):
        f = [data[j][i-j] for j in range(max(0,i-len_data+1), min(i+1,len_data))]
        amount_xmas += find_xmas("".join(f))
    r1 = amount_xmas

    r2 = 0
    for i in range(1,len_data-1):
        for j in range(1,len_data-1):
            if data[i][j] == "A":
                l1 = "".join([data[i-1][j-1],data[i][j],data[i+1][j+1]])
                l2 = "".join([data[i-1][j+1],data[i][j],data[i+1][j-1]])
                if (l1 == "MAS" or l1 == "SAM") and (l2 == "MAS" or l2 == "SAM"):
                    r2 += 1
    
    return r1, r2
