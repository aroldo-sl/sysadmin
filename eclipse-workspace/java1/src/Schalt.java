/* Programm zum bestimmen eines Schaltjahres.
 * 3. Aufgabe des Java 1 Projekts
 * von
 * Soner Karip 11114041 WI &
 * Phillip Rafat 11110000 WI
 */


// Import der Klasse Scanner aus dem unter package utility.
import java.util.Scanner;

public class Schalt
{
	// // Statische Main Methode mit einer IF-Anweisung zur Bestimmung des Schaltjahres.
	
	
	/**
	 * 
	 * @param args
	 */
	public static void main(String[] args)
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Geben Sie eine Jahr ein:");
		int x = s.nextInt();
		s.close();
       
		/* Notwendig aber nicht hinreichend: die Zahl(Jahr) muss durch 4 teilbar sein.
		 * Ausserdem darf die Zahl nicht durch 100 teilbar sein, es sei denn
		 * sie ist durch 400 teilbar.
		 */
		if( (x%4==0) && ((x%100!=0)||(x%400==0)))
		{
			System.out.println(x + " ist ein Schaltjahr!");
		}
		else
		{
			System.out.println(x + " ist kein Schaltjahr!");
		}
	
	}
}
