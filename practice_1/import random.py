import random

def cfg(name, rules):
    if isinstance(name, tuple):
        return cfg(random.choice(name), rules)
    if isinstance(name, list):
        return "".join([cfg(x, rules) for x in name])
    if name in rules:
        return cfg(rules[name], rules)
    else:
        return name

def test(rules, n):
    print("".join([cfg("S", rules) + "\n" for i in range(n)]))

g1 = {
    "K": [["("], ("S", ""), [")"]],
    "P": ("/", "+", "-", "-"),
    "Z": ("x", "y"),
    "S": [("K", ""), ("P", ""), ("Z", ""), ("S", "")]
}

test(g1, 5)