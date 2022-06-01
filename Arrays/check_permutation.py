def is_permutation(string_1, string_2):
    string_1 = string_1.replace(" ", "").lower()
    string_2 = string_2.replace(" ", "").lower()
    map = dict()
    for char in string_1:
        try:
            value = map[char]
            map[char] = value + 1
        except KeyError as e:
            map[char] = 1

    for char in string_2:
        try:
            value = map[char]
            if value == 1:
                map.pop(char)
            else:
                map[char] = value - 1
        except KeyError as e:
            return False
    if len(map) > 0:
        return False
    return True

if __name__ == "__main__":
    string_1, string_2 = input().split(",")
    print(is_permutation(string_1, string_2))