T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    print((N % K) + (N // K))
