# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:30:41 2019

@author: ajay_raikar
"""
# from collections import deque
import collections

class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]



example_graph = SimpleGraph()

# it is a directed graph
example_graph.edges = {
        'A':['B'],
        'B':['A', 'C', 'D'],
        'C':['A'],
        'D':['E', 'A'],
        'E':['B']
        }

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

def breadth_first_search_1(graph, start):
    # maintian a queue of frontiers
    frontier = Queue()
    # append start to Queue
    frontier.put(start)
    # maintain a dictionary of visited and if the node is visited then
    # mark it True start element will always visited first so make it True
    visited = {}
    visited[start] = True

    # while Queue is not empty do below process
    while not frontier.empty():
    # take a current node as first element from Queue and explore its
        current = frontier.get()
        print("Visiting %r"%current)
    # neighbors one by one and put them in Queue and repeat this process
        for next in graph.neighbors(current):
    # until the Queue is empty
            if next not in visited:
    # during this process mark the current node as visited
                visited[next] = True
                frontier.put(next)

breadth_first_search_1(example_graph, 'E')

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    # check whether the points are with-in the boundary or not
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    # check whether the points are in walls (obstable) or not if not they can
    # pass else they can't pass cause its blocked
    def passable(self, id):
        return id not in self.walls

    # find the neighbors of a node(represented as point in SquareGrid)
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]

        if (x+y)%2 == 0:results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

from implementation import *
g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS # list of walls
draw_grid(g)


# In order to reconstruct the paths we need to store the location of where
# we came from

def breadth_first_search_2(graph, start):
    # return came_from
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in came_from:
                came_from[next] = current
                frontier.put(next)
    return came_from



g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS

parents = breadth_first_search_2(g, (8, 7))
draw_grid(g, width=2, point_to=parents, start=(8, 7))









