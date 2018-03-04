# From Google foobar

"""
For each cell, store its state of row, col, and the number of walls it is
capable to remove on that point.

"""

from collections import deque


class Cell(object):
    def __init__(self, map, row, col, capable):
        self.map = map
        self.row = row
        self.col = col
        self.capable = capable

    def __hash__(self):
        return self.row ^ self.col ^ self.capable

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col \
               and self.capable == other.capable

    @property
    def neighbors(self):
        res = []
        m = len(self.map)
        n = len(self.map[0])
        for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nb_row, nb_col = self.row + dir[0], self.col + dir[1]
            if any([nb_row < 0, nb_row >= m, nb_col < 0, nb_col >= n]):
                continue
            is_nb_wall = self.map[nb_row][nb_col] == 1
            if not is_nb_wall:
                res.append(Cell(self.map, nb_row, nb_col, self.capable))
            else:
                if self.capable > 0:
                    res.append(
                        Cell(self.map, nb_row, nb_col, self.capable - 1))
        return res


def answer(map):
    start = Cell(map, 0, 0, 1)
    queue = deque([start])
    visited = {start: 1}

    while queue:
        current_cell = queue.popleft()
        if current_cell.row == len(map) - 1 \
                and current_cell.col == len(map[0]) - 1:
            return visited[current_cell]
        for nb in current_cell.neighbors:
            if nb in visited:
                continue
            queue.append(nb)
            visited[nb] = visited[current_cell] + 1

    return -1


print(answer([[0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1],
              [0, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0]]))

print(answer([[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 0],
              [0, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0]]))
