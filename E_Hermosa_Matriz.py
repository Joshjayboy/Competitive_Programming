def create_beautiful_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    current_number = 1
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                matrix[i][j] = current_number
                current_number += 1

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 != 0:
                matrix[i][j] = current_number
                current_number += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    cases = [int(data[i]) for i in range(1, t + 1)]
    
    results = []
    
    for n in cases:
        matrix = create_beautiful_matrix(n)
        results.append(matrix)
    
    for matrix in results:
        print_matrix(matrix)
        print()  # Print a blank line between test case outputs

if __name__ == "__main__":
    main()
