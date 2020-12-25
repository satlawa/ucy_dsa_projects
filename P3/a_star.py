# f_cost queue
from queue import PriorityQueue

def shortest_path(M,start,goal):
    print("shortest path called")
    accumulated_nodes, accumulated_cost = a_star(M, start, goal)
    path = get_path(accumulated_nodes, start, goal)
    return path


def calc_distance(start, end):
    '''
    Calculating the eucledian distance between two points
    '''
    dist = ((start[0] - end[0])**2 + (start[1] - end[1])**2)**(1/2)
    return dist


def a_star(node_map, start, goal):
    '''
    Implementation of the a-star algorithm
    '''
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

        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        print('current', current)
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

        # if goal is reached stop the loop
        if current == goal:
            break

        # loop through all the neighbouring nodes
        for neighbour in node_map.roads[current]:
            # calculate the cost (distance) from current node to neighbour node
            g_cost = accumulated_cost[current] + \
                calc_distance( node_map.intersections[current], \
                               node_map.intersections[neighbour])

            if (neighbour not in accumulated_cost) or (g_cost < accumulated_cost[neighbour]):
                # add/refresh path cost g for neighbour node
                accumulated_cost[neighbour] = g_cost
                # calculate estimated cost f = g + h
                f_cost = g_cost + calc_distance(node_map.intersections[neighbour], \
                                                node_map.intersections[goal])
                # add neighbour node with estimated total cost f to the priority queue
                frontier.put((f_cost, neighbour))
                # add/refresh visited nodes
                accumulated_nodes[neighbour] = current

    return accumulated_nodes, accumulated_cost


def get_path(accumulated_nodes, start, goal):
    '''
    Obtain list of nodes that have the minimum cost
    '''
    current= goal
    path = []
    while current:
        path.append(current)
        current = accumulated_nodes[current]
    path.reverse()
    return path
