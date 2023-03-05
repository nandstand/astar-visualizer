import pygame
import random
from tile import Tile


class Grid:
    WALL_DENSITY = 0.30  # percentage of grid to fill with wall tiles

    def __init__(self, window, rows, columns):
        self.window = window  # pygame window to draw to
        self.rows = rows  # number of rows in grid
        self.columns = columns  # number of columns in grid
        self.tiles = []  # the list that will hold the rows of tiles when the grid is populated

    def get_start(self):
        """returns the start tile"""
        return self.tiles[0][0]

    def get_end(self):
        """returns the end tile"""
        brx = self.columns - 1  # bottom right x
        bry = self.rows - 1  # bottom right y
        return self.tiles[brx][bry]

    def get_tiles(self):
        """returns the grid as a two-dimensional list"""
        return self.tiles

    def get_tile(self, x, y):
        """returns the tile at the given x,y coordinates"""
        return self.tiles[x][y]

    def draw(self):
        """draws the grid to the window provided at grid creation"""
        tile_width = self.window.get_width() // self.columns
        tile_height = self.window.get_height() // self.rows

        for row in self.tiles:
            for tile in row:
                x = tile.x * tile_width  # x position in terms of pixels
                y = tile.y * tile_height  # y position in terms of pixels
                rect = pygame.Rect(x, y, tile_width - 1, tile_height - 1)
                pygame.draw.rect(self.window, tile.get_type(), rect)

    # grid set up methods:

    def populate(self):

        # fill grid with unexplored tiles

        for i in range(self.rows):
            self.tiles.append([])
            for j in range(self.columns):
                new_tile = Tile(Tile.UNEXPLORED, i, j)
                self.tiles[i].append(new_tile)

        # set start tile

        self.tiles[0][0].set_type(Tile.START)

        # set end tile

        brx = self.columns - 1  # bottom right x
        bry = self.rows - 1  # bottom right y
        self.tiles[brx][bry].set_type(Tile.END)

        # randomly fill grid with certain percentage of wall tiles (WALL_DENSITY)

        num_tiles = self.rows * self.columns
        num_walls = int(num_tiles * Grid.WALL_DENSITY)
        for i in range(num_walls):
            row = random.choice(self.tiles)
            tile = random.choice(row)
            while tile.is_unexplored() == False:
                row = random.choice(self.tiles)
                tile = random.choice(row)
            tile.set_type(Tile.WALL)

    def setup_neighbors(self, x, y):

        has_left = not (x == 0)
        has_right = not (x == self.columns - 1)
        has_above = not (y == 0)
        has_below = not (y == self.rows - 1)

        tile = self.tiles[x][y]

        if has_left:
            left = self.tiles[x - 1][y]
            if not left.is_wall():
                tile.add_neighbor(left)

        if has_above:
            above = self.tiles[x][y - 1]
            if not above.is_wall():
                tile.add_neighbor(above)

        if has_below:
            below = self.tiles[x][y + 1]
            if not below.is_wall():
                tile.add_neighbor(below)

        if has_right:
            right = self.tiles[x + 1][y]
            if not right.is_wall():
                tile.add_neighbor(right)

    def build_graph(self):
        for x in range(0, self.columns):
            for y in range(0, self.rows):
                self.setup_neighbors(x, y)

    def reset(self):
        for row in self.tiles:
            for tile in row:
                if tile.is_closed() or tile.is_open() or tile.is_path():
                    tile.mark_unexplored()
