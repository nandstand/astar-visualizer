# astar-visualizer
Realtime visualizer for the A* pathfinding algorithm. 

This project is part of a study of the A* pathfinding algorithm, a flexible pathfinding algorithm widely used in games and other applications.  By comparing the performance and behavior of the A* algorithm with another, closely related pathfinding algorithm, Dijkstra’s algorithm, this project explores how A*’s accuracy and behavior can be tweaked by modifying its heuristic.  To accomplish this, each algorithm is applied to the task of finding the shortest path in a series of two-dimensional grids filled with randomly-placed obstacle tiles.  Demonstrates the effect of modifying A*’s heuristic to either be an underestimate or overestimate, with an overestimate producing behavior that does not guarantee the shortest path but does produce a “short enough” path with fewer operations.

![Demo screenshot](astar.PNG "Demo screenshot")
