N = int(input())

A = list(map(int, input().split()))

New_A = [elem * elem for elem in A]

for i in range(N):
    print(New_A[i], end = " ")