class Tile:

    # tile types:

    END = (255, 0, 0)  # RED
    START = (0, 255, 0)  # GREEN
    UNEXPLORED = (255, 255, 255)  # WHITE
    OPEN = (115, 156, 165)  # GRAY BLUE
    CLOSED = (110, 128, 128)  # GRAY
    WALL = (45, 45, 45)  # DARK GRAY
    PATH = (255, 165, 0)  # ORANGE

    def __init__(self, tile_type, x, y):
        self.tile_type = tile_type
        self.x = x
        self.y = y
        self.neighbors = []  # stores adjacent tiles

    def get_coords(self):
        return self.x, self.y

    def get_neighbors(self):
        return self.neighbors

    def add_neighbor(self, tile):
        self.neighbors.append(tile)

    def is_unexplored(self):
        return self.tile_type == Tile.UNEXPLORED

    def mark_unexplored(self):
        self.tile_type = Tile.UNEXPLORED

    def is_open(self):
        return self.tile_type == Tile.OPEN

    def mark_open(self):
        self.tile_type = Tile.OPEN

    def is_closed(self):
        return self.tile_type == Tile.CLOSED

    def mark_closed(self):
        self.tile_type = Tile.CLOSED

    def mark_path(self):
        self.tile_type = Tile.PATH

    def is_path(self):
        return self.tile_type == Tile.PATH

    def is_wall(self):
        return self.tile_type == Tile.WALL

    def is_start(self):
        return self.tile_type == Tile.START

    def is_end(self):
        return self.tile_type == Tile.END

    def get_type(self):
        return self.tile_type

    def set_type(self, tile_type):
        self.tile_type = tile_type

    def __lt__(self, other):
        return False