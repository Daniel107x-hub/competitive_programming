def is_palindrome(string, start, end):
    if end - start <= 1:
        return True
    return string[start] == string[end - 1] and is_palindrome(string, start + 1, end - 1)


if __name__ == "__main__":
    string = input()
    start = 0
    end = len(string)
    result = is_palindrome(string, start, end)
    print(result)