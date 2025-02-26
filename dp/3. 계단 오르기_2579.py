n = int(input())
stairs = [0]
for i in range(n):
    stairs.append(int(input()))

S = [0] * (n + 1)

if n >= 1:
    S[1] = stairs[1]
if n >= 2:
    S[2] = stairs[1] + stairs[2]
if n >= 3:
    S[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3]) 
if n >= 4:
    for i in range(4, n + 1):
        S[i] = max(S[i - 3] + stairs[i - 1] + stairs[i], S[i - 2] + stairs[i])

print(S[n])
