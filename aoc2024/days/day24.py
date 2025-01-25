from typing import List
from ..util import *
from python_mermaid.diagram import MermaidDiagram, Node, Link
from collections import defaultdict

gates_dict = dict()

def create_diagram(gates_dict: dict):
    nodes = defaultdict()
    for res, op in gates_dict.items():
        nodes[res] = Node(res)
        c1, c2 = op["childs"]
        nodes[c1] = Node(c1)
        nodes[c2] = Node(c2)

    links = list()
    count = 0
    for res, op in gates_dict.items():
        c1, c2 = sorted(op["childs"])
        ops = op["operator"]
        ops_node = Node(ops + str(count))
        nodes[(c1, c2, ops)] = ops_node
        links.append(Link(nodes[c1], ops_node))
        links.append(Link(nodes[c2], ops_node))
        links.append(Link(ops_node, nodes[res]))
        count += 1

    node_list = list()
    node_values = list(sorted(nodes.values(), key=lambda x: x.id))
    node_list.extend([n for n in node_values if n.id.startswith("x")])
    node_list.extend([n for n in node_values if n.id.startswith("y")])
    node_list.extend([n for n in node_values if n.id.startswith("z")])
    node_list.extend([n for n in node_values if n not in node_list])
    links.sort(key=lambda x: (x.origin.id, x.end.id))
    chart = MermaidDiagram(
        title="Gates",
        nodes=node_list,
        links=links,
    )
    with open("data/gate_chart.txt", "w+") as f:
        f.write(str(chart))


def parse_data(data: List[str]):
    splitpoint = data.index("")
    wires = dict()
    for d in data[:splitpoint]:
        w, b = d.split(": ")
        wires.update({w: int(b)})

    gates = list()
    for d in data[splitpoint+1:]:
        x, op, y, _, o = d.split()
        gates.append([x, y, op, o])

    return wires, gates

def operate(x, y, op):
    match op:
        case "AND": return x & y
        case "OR": return x | y
        case "XOR": return x ^ y

def get_sorted_wires(wires:dict, start:str):
    return dict(sorted({k: v for k, v in wires.items() if k.startswith(start)}.items(), reverse=True))

def get_joined_ints(ints: list[int]):
    return int("".join(list(map(str, ints))), 2)

def operate_gates(wires: dict, gates: list):
    wires_out = wires.copy()
    gates = gates.copy()
    i = 0
    while gates:
        gate = gates.pop(0)
        xv = wires_out.get(gate[0], None)
        yv = wires_out.get(gate[1], None)
        if xv is None or yv is None:
            gates.append(gate)
            if i > len(gates):
                return False
            i += 1
            continue
        i = 0
        r = operate(xv, yv, gate[2])
        wires_out.update({gate[3]: r})
    return wires_out

def res_1(wires, gates):
    wires_ = operate_gates(wires, gates)

    wires_z = get_sorted_wires(wires_, "z")
    return get_joined_ints(wires_z.values())

def swap_gates(g:list, indices:list):
    for i in indices:
        g[i[0]][3], g[i[1]][3] = g[i[1]][3], g[i[0]][3] 
    return g

def check_gates(gates:list, indices:list):
    for i in indices:
        if gates[i[0]][3] in gates[i[0]][:2]:
            return False
        if gates[i[1]][3] in gates[i[1]][:2]:
            return False
    return True

def res_2(wires: dict, gates: list):
    exp_z = get_joined_ints(get_sorted_wires(wires, "x").values()) + get_joined_ints(get_sorted_wires(wires, "y").values())
    c = [(18, 64), (55, 84), (108, 197), (116, 139)]
    gates = swap_gates(gates, c)
    swaped_gates = list()
    for i in c:
        swaped_gates.append(gates[i[0]][3])
        swaped_gates.append(gates[i[1]][3])
    global gates_dict
    gates_dict = {
        g[3]: 
        {
            "index": e,
            "operator": g[2],
            "childs": g[0:2],
        }
        for e, g in enumerate(gates)
    }
    create_diagram(gates_dict)

    # for i in range(1, 45):
    #     ws = get_wires(make_wire("z", i)) - get_wires(make_wire("z", i-1))
    #     print(f"wires of {make_wire("z", i)}")
    #     print("\n".join([print_con(wire) for wire in ws]))

    wires_ = operate_gates(wires, gates)
    wires_z = get_sorted_wires(wires_, "z")
    if get_joined_ints(wires_z.values()) == exp_z:
        return swaped_gates

def print_con(g):
    gs = gates_dict[g]
    c1, c2 = gs["childs"]
    return f"{g} = {c1} {gs["operator"]} {c2}"

def make_wire(var, num):
    return var + str(num).zfill(2)

def get_wires(w: str):
    res = set([w])
    c1, c2 = gates_dict[w]["childs"]
    if c1 in gates_dict:
        res |= get_wires(c1)
    if c2 in gates_dict:
        res |= get_wires(c2)
    return res
    

def execute(data: List[str], test_data: List[str]):
    wires, gates = parse_data(data)

    r1 = res_1(wires, gates)
    r2 = ",".join(list(sorted(res_2(wires, gates))))


    return r1, r2


# bpp OR ghf -> z06 64
# wvr XOR jgw -> fkp 18

# y31 AND x31 -> z31 55
# tpf AND mgq -> tkc 17
# mgq XOR tpf -> mfm 84

# y38 AND x38 -> bpt 197
# y38 XOR x38 -> krj 108

# jpp XOR stv -> ngr 116
# stv AND jpp -> z11 139
