from collections import deque

def sol(n, tree):
    q = deque([1])
    parent = [0] * (n+1)
    while q:
        cur = q.popleft()
        for i in tree[cur]:
            if parent[i] == 0 and i !=1:
                parent[i] = cur
                q.append(i)
    for i in range(2, n+1):
        print(parent[i])
        
if __name__ == "__main__":
    n = int(input())
    tree = dict()
    for i in range(1, n+1):
        tree[i] = []
    for _ in range(n-1):
        n1, n2 = map(int,input().split())
        tree[n1].append(n2)
        tree[n2].append(n1)
    sol(n, tree)