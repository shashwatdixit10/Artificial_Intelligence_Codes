class WampusWorld:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.kb = {}

    def update_perceptions(self, x, y, stench, breeze):
        self.grid[x][y] = 'S' if stench else 'B' if breeze else ' '

    def infer(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 'S':
                    self.kb[(i, j)] = 'Wampus'
                elif self.grid[i][j] == 'B':
                    self.kb[(i, j)] = 'Pit'

    def print_world(self):
        for row in self.grid:
            print(' '.join(row))

    def print_inferred_kb(self):
        print("Inferred Knowledge Base:")
        for pos, info in self.kb.items():
            print(f"At position {pos}: {info}")


world = WampusWorld(4)
world.update_perceptions(0, 0, True, False)
world.update_perceptions(1, 0, False, True)
world.print_world()
world.infer()
world.print_inferred_kb()
