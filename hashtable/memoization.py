

import math

##
my_arr = []
for i in range(100000):
    my_arr.append(i)
##
my_arr = [None] * 100000
for i in range(100000):
    my_arr[i] = i

## kind of an expensive computation with large x
def inverse_root(x):
    return 1/math.sqrt(x)

for i in(1, 100000):
    inverse_root(i)

## precalculated
def inverse_root(x):
    return 1/math.sqrt(x)
cache = {}
def build_lookup_table():
    for i in(1, 100000):
        cache[i] = inverse_root(i)

## suppose large numbers, user-facing
## how could we avoid runnign this computation at time of need? dont want a bad user experience

build_lookup_table()
### solves if users asks for a number we have not precalculated
def get_inverse_root(x):
    if x in cache:
        return cache[x]
    else:
        cache[x] = inverse_root(x)
        return cache[x]


print(cache[99999])
print(cache[100000])
print(get_inverse_root[99999])
print(get_inverse_root[100000])
