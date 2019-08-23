# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:40:20 2019

@author: ajay_raikar
"""

from implementation import *


def breadth_first_search_3(graph, start, goal):
    # return came_from
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                came_from[next] = current
                frontier.put(next)
    return came_from



s = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS
parents = breadth_first_search_3(g, (8, 7), (17, 2))
draw_grid(g, width=2, point_to=parents, start=(8,7), goal=(17, 2))
