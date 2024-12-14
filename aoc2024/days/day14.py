from typing import List
from ..util import *
import re
import matplotlib.pyplot as plt
import numpy as np


test_data = ["p=0,4 v=3,-3",
    "p=6,3 v=-1,-3",
    "p=10,3 v=-1,2",
    "p=2,0 v=2,-1",
    "p=0,0 v=1,3",
    "p=3,0 v=-2,-2",
    "p=7,6 v=-1,-3",
    "p=3,0 v=-1,-2",
    "p=9,3 v=2,3",
    "p=7,3 v=-1,2",
    "p=2,4 v=2,-3",
    "p=9,5 v=-3,-3",]

class Robot:
    def __init__(self, desc: str):
        self.p_x, self.p_y, self.v_x, self.v_y = list(map(int, re.findall(r"-?\d+", desc)))

    def move(self, field: tuple[int], times = 1):
        f_x, f_y = field
        self.p_x = (self.p_x + self.v_x * times) % f_x
        self.p_y = (self.p_y + self.v_y * times) % f_y


def execute(data: List[str]):
    def in_quadrant(robot: Robot, x: tuple[int], y: tuple[int]):
        return robot.p_x in range(x[0], x[1]) and robot.p_y in range(y[0], y[1])

    field = (101, 103)
    # data = test_data

    robots = [Robot(d) for d in data]
    for robot in robots:
        robot.move(field, 100)

    q1 = len([robot for robot in robots if in_quadrant(robot, (0, field[0]//2), (0, field[1]//2))])
    q2 = len([robot for robot in robots if in_quadrant(robot, (field[0]//2+1, field[0]), (0, field[1]//2))])
    q3 = len([robot for robot in robots if in_quadrant(robot, (0, field[0]//2), (field[1]//2+1, field[1]))])
    q4 = len([robot for robot in robots if in_quadrant(robot, (field[0]//2+1, field[0]), (field[1]//2+1, field[1]))])

    r1 = q1*q2*q3*q4
    r2 = 2


    return r1, r2
