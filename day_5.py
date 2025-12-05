with open("day_5_input.txt") as f:
    lines = f.read().strip().split("\n")
    ranges = [[int(r[0]), int(r[1])] for r in [ l.split('-') for l in lines if '-' in l]]
    ids = sorted([int(l) for l in lines if '-' not in l and len(l) > 0], reverse=True)

ranges.sort(key=lambda range: range[0])
merged = [ranges[0]]
for range in ranges[1:]:
    if range[0] <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], range[1])
    else:
        merged.append(range)

part_1 = 0
part_2 = 0
for range in merged:
    while len(ids) > 0 and ids[-1] <= range[1]:
        if ids.pop() >= range[0]:
            part_1 += 1

    part_2 += range[1] - range[0] + 1


print("Part 1:", part_1)
print("Part 2:", part_2)





