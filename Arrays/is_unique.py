def verify_is_unique(string):
    vector = [0 for i in range(0, 255)]
    chars = string.strip().replace(" ", "").lower()
    for char in chars:
        ascii_value = ord(char)
        vector_value = vector[ascii_value]
        if vector_value != 0:
            return False
        vector[ascii_value] = 1
    return True


if __name__ == "__main__":
    string = input()
    print(verify_is_unique(string))
