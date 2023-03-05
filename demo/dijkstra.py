from queue import PriorityQueue

from grid import *
from tile import Tile


def dijkstra(grid):
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

        if current != start:
            current.mark_closed()

        if current == end:
            path_len = build_path(grid, came_from)
            print("Dijkstra's path length: " + str(path_len))
            print("Dijkstra's total expanded: " + str(expanded))
            return True

        for next in current.get_neighbors():
            cost = g_cost[current] + 1
            if next not in g_cost or cost < g_cost[next]:
                g_cost[next] = cost
                open.put((cost, next))
                expanded += 1
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