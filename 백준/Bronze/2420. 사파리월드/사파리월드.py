N, M = map(int, input().split())
diff = 0

if N >= M:
    diff = N - M
else:
    diff = M - N

print(diff)