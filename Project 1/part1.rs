use std::env;

fn print_triangle(triangle:&Vec<Vec<i32>>, n:usize) {
    for i in 0..n {
        if i > 0 {
            println!();
        }
        for j in 0..=i {
            print!("{} ", triangle[i][j]);
        }
    }
}

fn generate_triangle(n:usize) -> Vec<Vec<i32>> {
    let mut triangle: Vec<Vec<i32>> = Vec::with_capacity(n);

    for i in 0..n {
        let mut row = vec![1; i + 1];
        for j in 1..i {
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
        triangle.push(row);
    }
    triangle
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let n: usize = args[1].parse().expect("Please provide an integer as the argument");
    let triangle = generate_triangle(n);
    print_triangle(&triangle, n);
}