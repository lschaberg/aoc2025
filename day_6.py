from math import prod

with open("day_6_input.txt") as f:
    lines = f.read().split("\n")
    grid = [[e.strip() if i == 4 else int(e.strip()) for e in l.split(' ') if not e == ''] for i, l in enumerate(lines)]

part_1 = 0
for i in range(len(grid[0])):
    if grid[4][i] == '+':
        part_1 += grid[0][i] + grid[1][i] + grid[2][i] + grid[3][i]
    else:
        part_1 += grid[0][i] * grid[1][i] * grid[2][i] * grid[3][i]

part_2 = 0
buffer = []
for i in range(len(lines[0]) - 1, -1, -1):
    col_str = "".join(lines[j][i] for j in range(4)).strip()
    if col_str == '':
        continue
    else:
        buffer.append(int(col_str))

    if lines[4][i] in ['+', '*']:
        if lines[4][i] == '+':
            part_2 += sum(buffer)
        else:
            part_2 += prod(buffer)
        buffer = []



print('Part 1:', part_1)
print('Part 2:', part_2)
