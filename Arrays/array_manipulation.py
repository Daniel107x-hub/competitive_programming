def array_manipulation(n, queries):
    arr = [0 for i in range(0, n + 1)]
    for query in queries:
        start, end, value = query
        for i in range(start, end + 1):
            arr[i - 1] = arr[i - 1] + value
    return max(arr)

def array_manipulation_optimized(n, queries):
    arr = [0 for i in range(0, n)]
    for query in queries:
        start, end, value = query
        arr[start - 1] += value
        arr[end] -= value
    max = None
    sum = None
    for i in range(0, n):
        if i == 0:
            max = arr[i]
            sum = max
        else:
            sum += arr[i]
            if sum > max:
                max = sum
    return max


if __name__ == "__main__":
    n, m = [int(i) for i in input().split(" ")]
    queries = []
    for i in range(0, m):
        queries.append([int(number) for number in input().split(" ")])
    result = array_manipulation(n, queries)
    print(result)
    result = array_manipulation_optimized(n, queries)
    print(result)

