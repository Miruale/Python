def f(x):
    d = 2
    while d ** 2 <= x:
        if x % d == 0:
            return 0
        d += 1
    return 1

k = int(input())
print(f(k))