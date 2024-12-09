from typing import List
from ..util import *
import sys

test_data = "2333133121414131402"
sys.set_int_max_str_digits(0)

def execute(data: List[str]):
    def id_gen():
        id = 0
        while True:
            yield id
            id += 1

    def operations():
        while True:
            yield add_file
            yield add_space

    def add_file(size):
        id = next(ids)
        filesystem_1.extend([id]*size)
        filesystem_2.append([id, size])
        filesizes[id] = size

    def add_space(size):
        filesystem_1.extend(["."]*size)
        filesystem_2.append([".", size])

    def defrag_complete(filesys: list):
        while filesys.count(".") > 0:
            file = filesys.pop()
            if file == ".": continue
            filesys[filesys.index(".")] = file
        return sum([e*f for e, f in enumerate(filesys)])
    
    def defrag_blockwise(filesys: list):
        for e in range(filesys[-1][0], 0, -1):
            size = filesizes[e]
            for i, p in enumerate(filesys):
                if p == [e, size]: break
                if (p[0] == ".") and (p[1] >= size):
                    p[1] -= size
                    ind = filesys.index([e, size])
                    filesys[ind][0] = "."
                    filesys.insert(i, [e, size])
                    break
        files = []
        for f in filesys:
            files.extend([f[0]]*f[1])
        files = [0 if i == "." else i for i in files]
        return sum([e*f for e, f in enumerate(files)])


    filesystem_1 = []
    filesystem_2 = []
    filesizes: dict = {}
    ids = id_gen()
    ops = operations()

    for d in data[0]:
        next(ops)(int(d))

    r1 = defrag_complete(filesystem_1)
    r2 = defrag_blockwise(filesystem_2)


    return r1, r2
