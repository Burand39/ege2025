from itertools import permutations
graph = 'AB BG GE EZ ZD DV BA GD BV'.split()
matrix = '67 567 456 35 234 123 12'.split()

for i in permutations('ABGEZVD'):
    res = []
    for x, y in graph:
        res.append(str(i.index(x)+1) in matrix[i.index(y)])
    if all(res):
        print(*i)