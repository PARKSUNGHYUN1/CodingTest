import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		String input = read.readLine();
		String[] in = input.trim().split(" ");
		int n = Integer.parseInt(in[0]);
		int m = Integer.parseInt(in[1]);
	
		BigInteger a = BigInteger.ONE;
		BigInteger b = BigInteger.ONE;
		BigInteger c = BigInteger.ONE;
	
		for(int i=0; i<n; i++) {
			a = a.multiply(new BigInteger(String.valueOf(n-i)));
		}
		
		for(int i=0; i<m; i++) {
			b = b.multiply(new BigInteger(String.valueOf(m-i)));
		}
		for(int i=0; i<n-m; i++) {
			c = c.multiply(new BigInteger(String.valueOf((n-m)-i)));
		}
		System.out.print(a.divide(b.multiply(c)));
	}
}