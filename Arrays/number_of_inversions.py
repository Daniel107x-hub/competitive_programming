def get_inversions(matrix):
    dimension = len(matrix)
    inversions = 0
    for p in range(0, dimension):
        for q in range(0, dimension):
            current_value = matrix[p][q]
            for i in range(0, p + 1):
                for j in range(0, q + 1):
                    if i == p and q == j:
                        break
                    compare_value = matrix[i][j]
                    if compare_value > current_value:
                        inversions += 1
    return inversions


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(0, test_cases):
        n = int(input())
        matrix = []
        for j in range(0, n):
            row = [int(n) for n in input().split(" ")]
            matrix.append(row)
        inversions = get_inversions(matrix)
        print(inversions)