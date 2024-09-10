memo = {}
def generate_pascals_triangle(n, k):
    if (n == 0) or (k == 0) or (k == n): return 1
    if (n,k) in memo: return memo[(n,k)]

    ret = generate_pascals_triangle(n-1, k-1) + generate_pascals_triangle(n-1, k)
    memo[(n,k)] = ret
    return ret

# Function to print the triangle as a matrix
def print_triangle(triangle):
    for row in triangle:
        print(row)

# Generate Pascal's Triangle for n rows

n = 40  # Example: 6 rows

for i in range(n):
    row = []
    for j in range(i+1):
        row.append(generate_pascals_triangle(i,j))
        
    print(row, '\n')
        
