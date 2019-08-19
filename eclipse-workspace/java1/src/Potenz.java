/* 
 * Programm zu rekusiven Berechnung einer Potenz.
 * 1. Aufgabe des Java 1 Projekts
 * von
 * Soner Karip 11114041 WI &
 * Phillip Rafat 11110000 WI
*/

// Import der Klasse Scanner aus dem unter package utility.
import java.util.Scanner;

public class Potenz 
{
	// Statische Main Methode mit dem Aufruf der Potenz Mehode. 
	public static void main (String[] args)
	{
		Scanner s = new Scanner(System.in);
				System.out.println("Geben Sie die Basis ein: ");
				int x = s.nextInt();
				System.out.println("Geben Sie die Potenz ein: ");
				int y = s.nextInt();
				System.out.println("Das Ergbnis der Potzen lautet:\n" + potenz(x,y));
				s.close();
	}
	
	// Statische Methode mit der Implementierug der Potenzierung. 
	private static int potenz(int a, int b)
	{
		if(b<1)
		{
			return 1;
		}
		/*
		 *return wird solange angehalten, bis der Ausdruck, wessen Rechenergebnis zurück-
		 *gegeben werden soll, zu Ende ausgerechnet wird. Insofern wird beim ersten Rekursions-
		 *aufruf return angehalten, um 'a' mit dem Rückgabewert des zweiten Aufrufs zu multipli-
		 *zieren. Aber der zweite Auruf wird auch angehalten, bis der dritte Aufruf einen
		 *Wert zurückgibt, usw, usf.
		 *Beim jedem Aufruf wird der Parameter 'b' deinkrementiert. Erst wenn 'b' den Wert 0
		 *hat, wird return nicht angehalten, sondern liefert den Wert 1.
		 */
		
		return a*potenz(a,b-1);
	}
}
