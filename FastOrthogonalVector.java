import java.util.Scanner;

public class FastOrthogonalVector {

    static final int M = 256;

    public static void readInput(long[][] A, Scanner sc) {
	    for (long[] a : A){
		    char[] s = sc.nextLine().toCharArray();
		    for (int i = 0; i < 4;i++){
			long addOne = 0b1;
			    for (int j = i*64+64-1;j>=i*64;j--) {
				if (s[j] == '1'){
					a[i]+=addOne;
				}
				addOne <<= 1;
			    }
		    }
	    }
    }

    public static boolean is_orthogonal(long[] u, long[] v) {
 	for (int i = 0; i < 4;i++){
		if ((u[i] & v[i]) != 0){
			return false;
		}
	}
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());

        long[][] A = new long[n][4];

        readInput(A, sc);

        long t = System.nanoTime();

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (is_orthogonal(A[i], A[j])) {
//                  System.out.println("yes");
        	    System.out.print("" + (System.nanoTime() - t) / 1e6);
                    System.exit(0);
                }
            }
        }

        System.out.print("" + (System.nanoTime() - t) / 1e6);


//      System.out.println("no");
    }
}
