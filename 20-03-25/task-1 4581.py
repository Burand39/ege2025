from itertools import permutations
graph = 'AD DE EG GC CF FA AB FB BE'.split()
matrix = '37 367 125 56 34 247 126'.split()
for i in permutations('ABCDEFG'):
    res = []
    for x, y in graph:
         res.append(str(i.index(x)+1) in matrix[i.index(y)])
    if all(res):
        print(*i)
