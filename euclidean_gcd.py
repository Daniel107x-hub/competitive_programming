def gcd(a, b):
    if b == 0:
        return a
    res = a % b
    return gcd(b, res)

print(gcd(357, 234))