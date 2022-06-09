def cyclic_shifts(bin, k):
    shifts = 0
    p = -1
    max = ""
    for i in range(0, len(bin)):
        if max < bin:
            max = bin
            shifts = i
        elif max == bin:
            p = i - shifts
            break
        bin = bin[1:] + bin[0]
    if p == -1:
        return shifts + (k - 1) * len(bin)
    else:
        return shifts + (k - 1) * p

if __name__ == "__main__":
    test_cases = int(input())
    for i in range(0, test_cases):
        n, k = [int(n) for n in input().split(" ")]
        bin = input()
        shifts = cyclic_shifts(bin, k)
        print(shifts)