"""
--- Day 7: Recursive Circus ---
https://adventofcode.com/2017/day/7

Do part 1 first to find the root node. Use the root to build a tree data
structure, then solve part 2. (Possible to build tree without finding root
node first but easier with, hence compromise solution. (In fact, tree not
actually necessary but makes part 2 neater; done just for interest too.))
"""

from collections import defaultdict
from itertools import chain
import re
from aocd import data


class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []

    @property
    def fullweight(self):
        return self.weight + sum(child.fullweight for child in self.children)


def parse(data):
    out = {}
    for line in data.splitlines():
        node, weight, *children = re.findall(r'\w+', line)
        out[node] = {'name': node, 'weight': int(weight), 'children': children}
    return out


def part1(nodes):
    # root is the only node which doesn't appear in `children` lists
    all_children = chain(*[nodes[node]['children'] for node in nodes])
    [root] = set(nodes) - set(all_children)
    return root


def part2(node, diff=0):
    # `child_weight_groups`: eg `{251: [<'ugml' node>], 243:[<'padx' node>,
    # <'fwft' node>]}` If there's more than one group then the (sub)tree is
    # unbalanced, the odd one out indicating the unbalanced branch.
    child_weight_groups = defaultdict(list)
    for child in node.children:
        child_weight_groups[child.fullweight].append(child)

    # `diff` will be reset to zero when we find the balanced children of the
    # target node, so calculate `corrected_weight` first.
    corrected_weight = node.weight - diff
    diff = max(child_weight_groups) - min(child_weight_groups)

    # target node found when we find its balanced children
    if not diff:
        return corrected_weight

    # else recurse down the unbalanced branch, maintaining `diff`
    for group in child_weight_groups.values():
        if len(group) == 1:
            return part2(group[0], diff=diff)


def treeify(nodes, node):
    node = nodes[node]
    tree = Node(node['name'], node['weight'])
    for child in node['children']:
        tree.children.append(treeify(nodes, child))
    return tree


if __name__ == '__main__':
    nodes = parse(data)
    root = part1(nodes)
    tree = treeify(nodes, root)
    print('Part 1:', root)
    print('Part 2:', part2(tree))
