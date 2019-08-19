/**
 * 
 */
package c4.median;

import java.util.Scanner;
/**
 * @author aroldo
 *
 */
public class Start {

	public static double[] fetchData(){
		double[] data;
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Wieviele Zahlen wollen Sie verarbeiten lassen?");
		int arrayLength = scan.nextInt();
		scan.close();
		data = new double[arrayLength];
		// TODO: fill the array
		return data;
	}
	
	/**
	 * Calculates the median of even and uneven lenth arrays.
	 * @param data
	 * @return
	 */
	public static double calcMedian(double[] data ){
		double m;
		int laenge;
		laenge = data.length;
		//TODO: clean up repetitions in data.
		
		if (data.length % 2==1){
			m = data[(laenge+1)/2-1];
		}
		else {m=0;} // false result.
		
		
		return m;};

	/**
	 * Test your functions here.
	 * 
	 */
	public static void someTests(){
		
		double[] data = fetchData();
		System.out.println("Sie wolllen " + data.length + " Zahlen verarbeiten lassen." );
        //TODO: test calcMedian
        	
	}
	/**
	 * Calculates the median of user data.
	 * @param args
	 */
	public static void main(String[] args) {
		// Try to implement as much as possible outside
		// this 'main' function.

		// someTests();

	}

}
