from itertools import permutations
graph = 'AC CE EG GF FA AB BF CD DH HE'.split()
matrix = '68 47 45 237 368 15 248 157'.split()

for i in permutations('ABCDEFGH'):
    res = []
    for x, y in graph:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)