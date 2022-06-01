def matching_strings(strings, queries):
    queries_map = dict()
    for query in queries:
        queries_map[query] = 0
    for string in strings:
        try:
            value = queries_map[string]
            queries_map[string] = value + 1
        except Exception as e:
            pass
    for query in queries:
        print(queries_map[query])

if __name__ == "__main__":
    n = int(input())
    strings = []
    for i in range(0, n):
        strings.append(input())
    n = int(input())
    queries = []
    for i in range(0, n):
        queries.append(input())
    matching_strings(strings, queries)