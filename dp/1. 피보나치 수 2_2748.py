def fibo(i):
    global F_cache    
    if F_cache[i] == -1:
        if i == 0 or i == 1:
            F_cache[i] = i
        else:
            F_cache[i] = fibo(i - 1) + fibo(i - 2)
        return F_cache[i]
    else:
        return F_cache[i]

n = int(input())
F_cache = [-1] * (n + 1)

print(fibo(n))
