with open("day_7_input.txt") as f:
    lines = f.read().strip().split("\n")

part_1 = 0
beams = [1 if char == 'S' else 0 for char in lines[0]]
for line in lines [1:]:
    for i, char in enumerate(line):
        if char == '^':
            if beams[i]:
                beams[i-1] += beams[i]
                beams[i+1] += beams[i]
                part_1 += 1
            beams[i] = 0


print('Part 1:', part_1)
print('Part 2:', sum(beams))