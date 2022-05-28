if __name__ == "__main__":
    n, queries = [int(n) for n in input().split(" ")]
    array = [list() for i in range(0, n)]
    answers = list()
    last_answer = 0
    for i in range(0, len(queries)):
        query_type, x, y = queries[i]
        if query_type == 1:
            index = (x ^ last_answer) % n
            array[index].append(y)
        elif query_type == 2:
            index = (x ^ last_answer) % n
            last_answer = array[index][y % len(array[index])]
            print(last_answer)
        else:
            pass
