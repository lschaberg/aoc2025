with open("day_4_input.txt") as f:
    grid = [[char for char in row] for row in f.read().strip().split("\n")]

def get_removable_indices(grid):
    indices = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == '@':
                adjacent = 0
                for i in range(max([0, x-1]), min([len(grid), x+2])):
                    for j in range(max([0, y-1]), min([len(row), y+2])):
                        if (i != x or j != y) and grid[i][j] == '@':
                            adjacent += 1
                if adjacent < 4:
                    indices.append((x, y))
    return indices

def remove_rolls(grid):
    indices = get_removable_indices(grid)
    if len(indices) == 0:
        return 0

    for index in indices:
        grid[index[0]][index[1]] = '.'

    return len(indices) + remove_rolls(grid)

print('Part 1:', len(get_removable_indices(grid)))
print('Part 2:', remove_rolls(grid))