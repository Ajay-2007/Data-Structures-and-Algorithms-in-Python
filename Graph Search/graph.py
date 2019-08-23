# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:04:19 2019

@author: ajay_raikar
"""


all_nodes = []
for x in range(20):
    for y in range(10):
        all_nodes.append([x, y])

# print(all_nodes)

def neighbors(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # think of this as a 2 coordinates axis x, y
    # [1, 0] -> right
    # [0, 1] -> up
    # [-1, 0] -> left
    # [0, -1] -> down
    result = []
    for dir in dirs:
        result.append(node[0] + dir[0], node[1]+dir[1])
    return result

# If your game allows diagonal movement, you’ll have eight entries in dirs.
# However, we want to return only the nodes that we can move to, so we’ll
# add a check:

def neighbors(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if neighbor in all_nodes:
            result.append(neighbor)
    return result


# An alternate way to check is to make sure the coordinates are in range.
# This only works if the map is rectangular. Here’s code for the 20x10 map
# we generated earlier:

def neighbors(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if 0 <= neighbor[0] < 20 and 0 <= neighbor[1] < 10:
            result.append(neighbor)
    return result














