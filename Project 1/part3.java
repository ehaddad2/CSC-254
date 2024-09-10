public class part3 {

	public int[][] fill_triangle(int n) {
		
		int[][] triangle = new int[n][n];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < i + 1; j++) {
				if (j == 0 || j == i) {
					triangle[i][j] = 1;
				}
				else {
					triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
				}
			}
		}
		
		print_triangle(triangle);	
		return triangle;		
	}
	
	public void print_triangle(int[][] triangle) {
		
		for (int i = 0; i < triangle.length; i++) {
			
			for (int j = 0; j < i + 1; j++) {
			   System.out.print(triangle[i][j] + " ");
			}
			System.out.println();
		}
	}
	
	public static void main(String[] args) {
		
		part3 run = new part3();
		int n = Integer.parseInt(args[0]);
		run.fill_triangle(n);
		
	}

}