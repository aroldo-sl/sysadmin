/* Programm zum sortieren eines Arrays.
 * 2. Aufgabe des Java 1 Projekts
 * von
 * Soner Karip 11114041 WI &
 * Phillip Rafat 11110000 WI
 */

// Import der Klasse Scanner aus dem unter package utility.
import java.util.Scanner;

public class Sortieren 
{
	/**
	* 
	* @param args
	* Diese Methode ruft die statische Methode bubblesSort auf.
	*/
	
	// Statische Main Methode für festlegung der groesse eines Array und dem Aufruf von Bubblesort.
	public static void main(String[] args)
	{
		Scanner s = new Scanner(System.in);
		
		// Eingabe der Länge des Arrays
		System.out.print("Wieviel Werte moechten Sie eingeben?:");
		int x = s.nextInt();
		
		int y;// Deklaraation eine weiter unten im Code eingesetzten Variablen.
		
		// Erstellung eines Arrays der Länge x.
		int[] a = new int[x];
		
		// Eingabe der unsortierten Werte des Arrays.
		for(int i = 0; i<x; i++)
		{
			int p = i +1;
			System.out.print("Geben Sie eine Zahl fuer den " +p+  ". Platz im Array ein: " );
			y = s.nextInt();
			a[i] = y;
			System.out.println();
		}
		s.close(); //Das Objekt Scanner wird ab hier geschlossen.
		
		// Ausgaabe der Werte des Arrays vor der Sortierung.
		System.out.println("\n======Unsortiert======");
		for(int i = 0; i<x; i++)
		{
			System.out.print(a[i] + " ");
		}
	
		System.out.println();
		
		/**
		* Der Aufruf der Methode bubbleSort mit dem Array als Parameter ändert den
		* Zustand des Arrays INPLACE. Also kann das gleiche Array nach der Ausführung
		* von bubbleSort weiter im Code eingesetzt werden, mit dem Unterschied, dass
		* das Array dann sortiert ist.
		*/
		
		bubbleSort(a);
		
			// Ausgabe des Sortierten Arrays.
			System.out.println("\n=======Sortiert=======");
		for(int o = 0; o<a.length; o++)
		{
			System.out.print(a[o]+ " ");
		}
		
	}	
	
	/**
	* INPLACE-Sortierung, also: der Eingabeparameter ist das Array,
	* das sortiert werden soll. Die Methode gibt nichts zurück.
	* Die Methode ist statisch, kann also ohne vorherige instantiierung eines Objekts
	* aufgerufen werden.
	*/
	public static void bubbleSort(int[] a)
	{
	  int b; // Zwischhenspeicher für den Swap.
	
	  /**
	  * Der Index der äußeren Schleife fäng maximal an (letzter Index
	  * des Arrays +1) und wird bis zum zweiten Index des Arrays (Index = 1)
	  * nach jedem Schleifendurchlauf dekrementiert. 
	  */
	  for (int n=a.length; n>1; n=n-1)
	  {
		  /**
		  * Der Index der inneren Schleife fängt immer bei Null an und
		  * wird bei jedem Durchlauf der inneren Schleife um 1 inkreementiert
		  * Die obere Grenze des Laufiindex der inneren Schleife (N-1) ist nach jedem
		  * Durchlauf der äußeren Schhleife kleiner, weil n nach jedem Durchlauf der
		  * äußeren Schleife um1 kleiner wird.
		  */  
	    for (int i=0; i<n-1; i=i+1)
	    {	
	      if (a[i] > a[i+1])
	      {
	    	  /**
	    	  * SWAP a[i], a[i+1]
	    	  * Wenn für zwei Nachbarwerte des Arrays die Reihenfolge nicht stimmt (siehe
	    	  * Bedingung im Kopf des if-Blocks),
	    	  * dann werden die zwei Werte gegeneinander ausgetauscht.
	    	  */  
	        b=a[i]; // der Wert an der i-ten Stelle ist in b zwischengespeiichert.
	        
	        a[i]=a[i+1]; // die Werte an der i-ten und an der (i+1)-ten Stelle wurden gleichgesetzt.
	        
	        a[i+1]=b; // der zwiischengespeicherter ursprünglicher Wert von a[i]
	        		 // wird nach der (i+1)-ten Stelle übertragen.
	      } // ende if
	    } // ende innere for-Schleife
	  } // ende Aussere for-Schleife
	}
}

