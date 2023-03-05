from astar import *
from dijkstra import *

# pygame window setup

WIN_WIDTH = 800
WIN_HEIGHT = 800
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
window.fill((128, 128, 128))  # fill window with background color

# grid setup

GRID_ROWS = 80
GRID_COLUMNS = 80
grid = Grid(window, GRID_ROWS, GRID_COLUMNS)

# demo

found = False
while not found:
    grid = Grid(window, GRID_ROWS, GRID_COLUMNS)
    grid.populate()  # build and randomize the grid
    grid.build_graph()  # set up each tile with its neighboring tiles
    found = dijkstra(grid)
pygame.time.delay(3000)
grid.reset()
astar_under(grid)
pygame.time.delay(3000)