H, M = map(int, input().split())
M -= 45
if M < 0:
    H -= 1
    if H < 0:
        H += 24
    M += 60
print('{} {}'.format(H, M))
