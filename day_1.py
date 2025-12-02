with open("day_1_input.txt") as f:
    lines = f.read().strip().split("\n")

mod = 100
dial = 50
part_1 = 0
part_2 = 0
for line in lines:
    sign = 1 if line[0] == "R" else -1
    num = int(line[1:])
    part_2 += ((dial if sign == 1 else (mod - dial) % mod) + num) // mod
    dial = (dial + sign * num) % mod
    if dial == 0:
        part_1 += 1

print("Part 1:", part_1)
print("Part 2:", part_2)