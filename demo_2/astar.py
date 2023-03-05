from queue import PriorityQueue

from grid import *
from tile import Tile


def h_man(tile_1, tile_2):
    # h-score using manhattan distance, no diagonal movement

    x1, y1 = tile_1.get_coords()
    x2, y2 = tile_2.get_coords()
    h = abs(x1 - x2) + abs(y1 - y2)
    return h

def h_man_over(tile_1, tile_2):
    # h-score using manhattan distance, no diagonal movement

    x1, y1 = tile_1.get_coords()
    x2, y2 = tile_2.get_coords()
    h = abs(x1 - x2) + abs(y1 - y2)
    return h * 1.05

def h_man_under(tile_1, tile_2):
    # h-score using manhattan distance, no diagonal movement

    x1, y1 = tile_1.get_coords()
    x2, y2 = tile_2.get_coords()
    h = abs(x1 - x2) + abs(y1 - y2)
    return h * 0.65

def astar(grid):
    open = PriorityQueue()
    start = grid.get_start()
    open.put((0, start))

    came_from = {}
    g_cost = {}

    came_from[start] = None
    g_cost[start] = 0

    end = grid.get_end()
    start = grid.get_start()

    expanded = 0

    while not open.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open.get()[1]

        if current == end:
            path_len = build_path(grid, came_from)
            print("A* path length: " + str(path_len))
            print("A* total expanded: " + str(expanded))
            return True

        if current != start:
            current.mark_closed()

        for next in current.get_neighbors():
            cost = g_cost[current] + 1
            if next not in g_cost or cost < g_cost[next]:
                g_cost[next] = cost  # we found a shorter path from start
                f_cost = cost + h_man(next, end)
                open.put((f_cost, next))
                expanded += 1
                if (next != end):
                    next.mark_open()
                came_from[next] = current

        grid.draw()
        pygame.display.flip()

    return False

def astar_over(grid):
    open = PriorityQueue()
    start = grid.get_start()
    open.put((0, start))

    came_from = {}
    g_cost = {}

    came_from[start] = None
    g_cost[start] = 0

    end = grid.get_end()
    start = grid.get_start()

    expanded = 0

    while not open.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open.get()[1]

        if current == end:
            path_len = build_path(grid, came_from)
            print("A* path length: " + str(path_len))
            print("A* total expanded: " + str(expanded))
            return True

        if current != start:
            current.mark_closed()

        for next in current.get_neighbors():
            cost = g_cost[current] + 1
            if next not in g_cost or cost < g_cost[next]:
                g_cost[next] = cost  # we found a shorter path from start
                f_cost = cost + h_man_over(next, end)
                open.put((f_cost, next))
                expanded += 1
                if (next != end):
                    next.mark_open()
                came_from[next] = current

        grid.draw()
        pygame.display.flip()

    return False

def astar_under(grid):
    open = PriorityQueue()
    start = grid.get_start()
    open.put((0, start))

    came_from = {}
    g_cost = {}

    came_from[start] = None
    g_cost[start] = 0

    end = grid.get_end()
    start = grid.get_start()

    expanded = 0

    while not open.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open.get()[1]

        if current == end:
            path_len = build_path(grid, came_from)
            print("A* path length: " + str(path_len))
            print("A* total expanded: " + str(expanded))
            return True

        if current != start:
            current.mark_closed()

        for next in current.get_neighbors():
            cost = g_cost[current] + 1
            if next not in g_cost or cost < g_cost[next]:
                g_cost[next] = cost  # we found a shorter path from start
                f_cost = cost + h_man_under(next, end)
                open.put((f_cost, next))
                expanded += 1
                if (next != end):
                    next.mark_open()
                came_from[next] = current

        grid.draw()
        pygame.display.flip()

    return False


def build_path(grid, came_from):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    path_len = 0
    curr = grid.get_end()
    while curr in came_from:
        curr = came_from[curr]
        if curr is not None:
            path_len += 1
            curr.mark_path()
            grid.draw()
            pygame.display.flip()

        start = grid.get_start()
        end = grid.get_end()

        start.set_type(Tile.START)
        end.set_type(Tile.END)

    grid.draw()
    pygame.display.flip()

    return path_len
