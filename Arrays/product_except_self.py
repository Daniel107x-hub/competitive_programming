def array_except_self(a):
    before = [0] * len(a)
    after = [0] * len(a)
    acc = 1
    for i in range(0, len(a)):
        before[i] = acc
        acc *= a[i]
    acc = 1
    for i in range(len(a)-1, -1, -1):
        after[i] = acc
        acc *= a[i]
    result = [0] * len(a)
    for i in range(0, len(a)):
        result[i] = before[i] * after[i]
    return result


if __name__=='__main__':
    a = [int(n) for n in input().split(",")]
    result = array_except_self(a)
    print(result)