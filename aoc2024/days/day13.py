from typing import List
from ..util import *

test_data = [
    "Button A: X+94, Y+34",
    "Button B: X+22, Y+67",
    "Prize: X=8400, Y=5400",
    "    ",
    "Button A: X+26, Y+66",
    "Button B: X+67, Y+21",
    "Prize: X=12748, Y=12176",
    "    ",
    "Button A: X+17, Y+86",
    "Button B: X+84, Y+37",
    "Prize: X=7870, Y=6450",
    "    ",
    "Button A: X+69, Y+23",
    "Button B: X+27, Y+71",
    "Prize: X=18641, Y=10279",
    "    ",
    ]


class Button:
    def __init__(self, desc: str):
        self.x = int(desc[12:14])
        self.y = int(desc[18:20])

class Prize:
    def __init__(self, desc: str):
        atts = desc.split()
        self.x = int(atts[1][2:-1])
        self.y = int(atts[2][2:])

class ClawMachine:
    def __init__(self, desc: List[str]):
        self.a = Button(desc[0])
        self.b = Button(desc[1])
        self.p = Prize(desc[2])
        self.costs = self.calc_dirs()
        self.costs_n = self.calc_dirs(10000000000000)
        
    def calc_dirs(self, size = 0):
        prize_x = self.p.x + size
        prize_y = self.p.y + size
        d = self.a.x*self.b.y - self.a.y*self.b.x
        a = abs(int((prize_x*self.b.y - prize_y*self.b.x)/d))
        b = abs(int((prize_y*self.a.x - prize_x*self.a.y)/d))
        if (self.a.x * a + self.b.x * b, self.a.y * a + self.b.y * b) == (prize_x, prize_y):
            return int(b + a*3)
        return 0


def execute(data: List[str]):
    claw_machines: list[ClawMachine] = []
    for a, b, p, _ in zip(*[iter(data)]*4):
        claw_machines.append(ClawMachine([a,b,p]))

    r1 = sum([cm.costs for cm in claw_machines])
    r2 = sum([cm.costs_n for cm in claw_machines])

    return r1, r2
