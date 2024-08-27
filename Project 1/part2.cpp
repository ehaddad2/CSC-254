#include <iostream>
#include <stdlib.h>
using namespace std;

void print_triangle(int** triangle, int n) {
    for(int i = 0; i < n; i++) {
        if (i > 0) cout << "\n";
        for(int j = 0; j <= i; j++) {
            cout << triangle[i][j] << " ";
        }
    }
}

int** generate_triangle(int n) {
    int** triangle = new int* [n];

    for(int i=0; i < n; i++) {
        //init each row
        triangle[i] = new int[i+1];
        triangle[i][0] = 1;
        triangle[i][i] = 1;

        //calculate vals using adj entries
        for (int j = 1; j < i; j++) {
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
        }
    }
    return triangle;
}

int main(int argc, char* argv[])
{
    int n = atoi(argv[1]);
    int** triangle = generate_triangle(n);
    print_triangle(triangle, n);
}
