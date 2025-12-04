with open("day_3_input.txt") as f:
    banks = f.read().strip().split("\n")

def max_joltage_str(bank: str, n: int):
    if n == 1:
        return max(bank)
    _max = max(bank[:-n+1])
    return _max + max_joltage_str(bank[bank.index(_max)+1:], n-1)


part_1 = 0
part_2 = 0
for bank in banks:
    part_1 += int(max_joltage_str(bank, 2))
    part_2 += int(max_joltage_str(bank, 12))

print('Part 1:', part_1)
print('Part 2:', part_2)
