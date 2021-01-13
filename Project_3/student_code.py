# imports
from queue import PriorityQueue


def calc_distance(start, end):
    '''
    Calculating the eucledian distance between two points

    Args:
        start(list): list of two floats representing x and y coordinates of the start point
        end(list): list of two floats representing x and y coordinates of the end point
    Returns:
        float: eucledian distance
    '''
    dist = ((start[0] - end[0])**2 + (start[1] - end[1])**2)**(1/2)

    return dist


def shortest_path(M, start, goal):
    '''
    Implementation of the a-star algorithm to find the path with the minimum total cost
    given a map (graph), a start node and goal node

    Args:
        M(Map): a graph with nodes and their connnections
        start(int): number of start node
        goal(int): number of goal node
    Returns:
        list: list with the order of nodes that give the shortest path
    '''

    print("shortest path called")
    # frontier for keepeing the nodes to explore in an orderd list
    frontier = PriorityQueue()
    # add start node with f-cost of 0 to queue
    frontier.put((0, start))

    # to keep track of the nodes visited
    accumulated_nodes = {}
    accumulated_nodes[start] = None

    # to keep track of the total cost
    accumulated_cost = {}
    accumulated_cost[start] = 0

    # loop as long as there are nodes to explore
    while not frontier.empty():
        # get next node with smallest cost
        _, current = frontier.get()

        # if goal is reached stop the loop
        if current == goal:
            break

        # loop through all the neighbouring nodes
        for neighbour in M.roads[current]:
            # calculate the cost (distance) from current node to neighbour node
            g_cost = accumulated_cost[current] + \
                calc_distance( M.intersections[current], \
                               M.intersections[neighbour])

            if (neighbour not in accumulated_cost) or (g_cost < accumulated_cost[neighbour]):
                # add/refresh path cost g for neighbour node
                accumulated_cost[neighbour] = g_cost
                # calculate estimated cost f = g + h
                f_cost = g_cost + calc_distance(M.intersections[neighbour], \
                                                M.intersections[goal])
                # add neighbour node with estimated total cost f to the priority queue
                frontier.put((f_cost, neighbour))
                # add/refresh visited nodes
                accumulated_nodes[neighbour] = current

    # list for holding min cost path
    min_cost_path = []
    current = goal
    # reconstruct path from accumulated_nodes
    while current:
        min_cost_path.append(current)
        current = accumulated_nodes[current]
    # reverse path meet condition: start to goal
    min_cost_path.reverse()

    return min_cost_path
