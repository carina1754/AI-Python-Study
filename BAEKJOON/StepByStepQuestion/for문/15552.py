import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    A, B = map(int, sys.stdin.readline().split())
    print('{}'.format(A+B))