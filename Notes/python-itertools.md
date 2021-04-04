# zip & itertools.zip_longest(* iterables, fillvalue=None)

# `itertools.product(*iterables, repeat=1)`
## 二维遍历
> product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
> product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111

Cartesian product of input iterables.
Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same as ((x,y) for x in A for y in B).





# `itertools.combinations(iterable, r)`
## 排列组合,非重复
> combinations('ABCD', 2) --> AB AC AD BC BD CD
> combinations(range(4), 3) --> 012 013 023 123


Return r length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sort order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Elements are treated as unique based on their position, not on their value. So if the input elements are unique, there will be no repeat values in each combination.

Roughly equivalent to:

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


# permutations(iterable, r=None) 排列组合
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210