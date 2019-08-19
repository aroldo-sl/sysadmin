/**
 * Should contain a class with the 'main' static method.
 * 
 */
package entry_point;

// Some unnecessary imports
import java.lang.String;
import java.lang.System;
//


/**
 * @author aroldo
 *
 * contains the 'main' method.
 */
public class Main {

	/**
	 * This method is like the 'main' function in C.
	 * @param argv
	 */
	
	public static void main(String[] argv) {
		// argv is an array with the command line input parameters.
		
		System.out.println("Hello Crazy World!");
		System.out.println("You gave me this number of parameters:");
		System.out.println(argv.length);
		for(int i=0; i<argv.length;i++)
			{System.out.println("Hallo " + argv[i] +"!");
		}
		
	}

}
