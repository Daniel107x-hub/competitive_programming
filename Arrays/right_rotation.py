def right_rotate(arr, k):
    rotated_arr = [0 for i in range(0, len(arr))]
    for i in range(0, len(arr)):
        new_pos = (i + k) % len(arr)
        rotated_arr[new_pos] = arr[i]
    for element in rotated_arr:
        print(element, end=" ")

if __name__ == "__main__":
    test_cases = int(input())
    for i in range(0, test_cases):
        n, k = [int(n) for n in input().split(" ")]
        arr = [int(n) for n in input().split(" ")]
        right_rotate(arr, k)

