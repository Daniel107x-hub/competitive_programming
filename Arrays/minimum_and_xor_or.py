def xor(a, b):
    tmp_a = format(a, 'b')
    tmp_b = format(b, 'b')
    return int((tmp_a & ~tmp_b) | (~tmp_a & tmp_b), 2)

def minimum(arr):
    min = None
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            value = xor((arr[i] or arr[j]), (arr[i] and arr[j]))
            if j == 0 and i == 0 or value < min:
                min = value
    return min


if __name__ == "__main__":
    cases = int(input())
    for i in range(0, cases):
        n = input()
        arr = [int(number) for number in input().split(" ")]
        result = minimum(arr)
        print(result)