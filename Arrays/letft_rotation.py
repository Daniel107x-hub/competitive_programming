def rotate_left(d, arr):
    new_arr = [0 for n in arr]
    for i in range(0, len(arr)):
        new_position = (i - d) % len(arr)
        new_arr[new_position] = arr[i]
    return new_arr


if __name__ == "__main__":
    arr_size, d = [int(n) for n in input().split(" ")]
    arr = [int(n) for n in input().split(" ")]
    result = rotate_left(d, arr)
    print(result)
