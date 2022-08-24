from itertools import combinations
n, m = map(int, input().split())
arr =[]
for i in range(0, n):
    arr.append(i+1)
result = list(combinations(arr, m))
for i in range(0, len(result)):
    for j in range(0, m):
        print(result[i][j], end=' ')
    print()