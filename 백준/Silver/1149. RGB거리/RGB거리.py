n = int(input())
st = []
for i in range(n):
    st.append(list(map(int, input().split())))
for i in range(1, len(st)):
    st[i][0] += min(st[i - 1][1], st[i - 1][2])
    st[i][1] += min(st[i - 1][0], st[i - 1][2])
    st[i][2] += min(st[i - 1][0], st[i - 1][1])
print(min(st[n-1]))
