"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
sums = {}
differences = {}
f_results = {}

for x in q:
    fx = f(x)

    for y in q:
        fy = f(y)

        x_plus_y = fx + fy
        if x_plus_y not in sums:
            sums[x_plus_y] = set()
        sums[x_plus_y].add((x, y))

        x_minus_y = fx - fy
        if x_minus_y not in differences:
            differences[x_minus_y] = set()
        differences[x_minus_y].add((x, y))

        y_minus_x = fy - fx
        if y_minus_x not in differences:
            differences[y_minus_x] = set()
        differences[y_minus_x].add((y, x))


for value in sums:
    if value not in differences:
        continue

    for a, b in sums[value]:
        for c, d in differences[value]:
            print(f"f({a}) + f({b}) = f({c}) - f({d})",end='\t')
            print(f"{f(a)} + {f(b)} = {f(c)} + {f(d)}")
