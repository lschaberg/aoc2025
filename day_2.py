with open("day_2_input.txt") as f:
    ranges = f.read().strip().split(",")

mods = range(2, max([len(r) // 2 for r in ranges]))
part_1 = 0
part_2_set = set()
for mod in mods:
    for r in ranges:
        [start, end] = r.split("-")
        # find even numbers in [start # digits, end # digits]
        # middle condition: for i in range(1[n-1 zeroes],9[n-1 nines]) p1 += i * 10 ^ n + i
        # start boundary condition: if snd is even, start range at start // 10 ^ n, subtract 1 if start % 10 ^ n is greater
        ns = [i // mod for i in range(len(start), len(end) + 1) if i % mod == 0]
        for n in ns:
            n_start = 10**(n-1)
            n_remainder = 10**(n * (mod - 1))
            print(n, len(start), mod)
            if n == len(start) / mod:
                n_start = int(start) // n_remainder
                for segment in [int(start) % 10**(n*i) // 10**(n*(i-1)) for i in range(mod-1, 0, -1)]:
                    print(segment)
                    if segment > n_start:
                        n_start += 1
                        break
                    elif segment < n_start:
                        break
            n_end = (10**n - 1)
            if n == len(end) / mod:
                n_end = int(end) // n_remainder
                for segment in [int(end) % 10**(n*i) // 10**(n*(i-1)) for i in range(mod-1, 0, -1)]:
                    print("2", segment, n_end)
                    if segment < n_end:
                        n_end -= 1
                        break
                    elif segment > n_end:
                        break
            print(f"{r=}, {n_start=}, {n_end=}, {n_remainder=}")
            for i in range(n_start, n_end + 1):
                print(f"{r=}, {n_start=}, {n_end=}, {i=}")
                invalid_num = int(str(i) * mod)
                if mod == 2:
                    part_1 += invalid_num
                part_2_set.add(invalid_num)

print("Part 1:", part_1)
print("Part 2:", sum(part_2_set))


