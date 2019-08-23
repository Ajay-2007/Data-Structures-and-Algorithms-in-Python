# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:48:34 2019

@author: ajay_raikar
"""

from queue import Queue, PriorityQueue


frontier = Queue()

frontier.put(start) # appending start position to the Queue

visited = {}
visited[start] = True

while not frontier.empty():
    current = frontier.get()
    for next in graph.neighbors(current):
        if next not in visited:
            frontier.put(next)
            visited[next] = True

# Modifying the loop to keep track of where we came from for every location
# that's visited and rename the visited to a came_from table

frontier = Queue()
frontier.put(start)
came_from = {} # came_from for each location points to the place where we came
# from
came_from[start] = None

while not frontier.empty():
    current = froniter.get()
    for next in graph.neighbours(current):
        if next not in came_from:
            frontier.put(next)
            came_from[next] = current


# To reconstruct path we follow the table came_from to see where we came
# from and put it in a list and reverse the list
# This will give us the path from where we came from
current = goal
path = []
while current != start:
    path.append(current)
    current = came_from[current]
path.append(start) # this will give us path from goal->start
paht.reverse() # this will give us path from start-> goal



# Early exit
# We’ve found paths from one location to all other locations. Often we don’t
# need all the paths; we only need a path from one location to one other
# location. We can stop expanding the frontier as soon as we’ve found our goal.

frontier = Queue()
frontier.put(start)
came_from = {}
came_from[start] = None

while not frontier.empty():
    current = frontier.get()

    if current == goat:
        break

    for next in graph.neighbors(current):
        if next not in came_from:
            froniter.put(next)
            came_from[next] = current


# Movement costs
# We need to track movement costs,
# We want to take the movement costs into account when deciding how to evaluate
# locations; let’s turn our queue into a priority queue. Less obviously, we may
# end up visiting a location multiple times, with different costs, so we need to
# alter the logic a little bit. Instead of adding a location to the frontier if
# the location has never been visited, we’ll add it if the new path to the
# location is better than the best previous path.

frontier = PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
    current = frontier.get()

    if current == goal:
        break

    for next in graph.neighbors(current):
        new_cost = cost_so_far[current] + graph.cost(current, next)
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost
            frontier.put(next, priority)
            came_from[next] = current














