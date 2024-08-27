def generate_pascals_triangle(n):
    # Create an empty list to store the rows of Pascal's Triangle
    triangle = []

    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)

        # Calculate the inner elements of the row using the sum of elements from the previous row
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        # Add the row to the triangle
        triangle.append(row)

    return triangle

# Function to print the triangle as a matrix
def print_triangle(triangle):
    for row in triangle:
        print(row)

# Generate Pascal's Triangle for n rows
n = 6  # Example: 6 rows
pascals_triangle = generate_pascals_triangle(n)
print_triangle(pascals_triangle)