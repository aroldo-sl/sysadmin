
import java.util.*;

/**
 * 
 * @author aroldo
 *
 * Diese Klasse hat zwei statische Methoden.
 */
public class Sortieren2 
{
	
	/**
	 * 
	 * @param args
	 * 
	 * Diese Methode ruft die statische Methode bubblesSort auf.
	 */
	public static void main(String[] args)
	{
		Scanner s = new Scanner(System.in);
		
		// Eingabe der Länge des Arrays
		System.out.println("Wieviel Werte m�chten Sie eingeben? :");
		int x = s.nextInt();
		//
		
		
		int y; // Deklaraation eine weiter unten im Code eingesetzten Variablen.
		
		/**
		 * Zwei Befehle in einemr:
		 * int[] a;
		 * a = new int[x]; // Erstellung eines Arrays der Länge x.
		 */
		int[] a = new int[x];
		
		
		// Eingabe der unsortierten Werte des Arrays
		for(int i = 0; i<x; i++)
		{
			System.out.print("Geben Sie eine Zahl f�r den" + i + "Platz im Array ein: " );
			y = s.nextInt();
			a[i] = y;
			System.out.println();
	
		}
		//
		
		s.close(); //Der Scanner wird ab hier nicht mehr gebraucht.
		
		// Ausgaabe der Werte des Arrays vor der Sortierung.
		System.out.println("====Unsortiert====");
		for(int i = 0; i<x; i++)
		{
			System.out.print(a[i] + " ");
		}
		//
	
		System.out.println(); // Leerzeile ausdrucken.
		
		//  Sortierung.
		/**
		 * Der Aufruf der Methode bulleSort mit dem Array als Parameter ändert den
		 * Zustand des Arrays INPLACE. Also kann das gleiche Array nach der Ausführung
		 * von bubbleSort weiter im Code eingesetzt werden, mit dem Unterschied, dass
		 * das Array dann sortiert ist.
		 */
		bubbleSort(a);
		// 
		
		
		// Ausgabe des Sortierten Arrays.
		System.out.println("====Sortiert====");
		for(int o = 0; o<a.length; o++)
		{
			System.out.println(a[o]);
		}
		//
		
	}	
	
         /**
	 * INPLACE-Sortierung, also: der Eingabeparameter ist das Array,
	 * das sortiert werden soll. Die Methode gibt nichts zurück.
	 * 
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
		   * wird bei jedem Durchlauf der inneren Schleife um 1 inkreementiert.
		   * Die obere Grenze des Laufiindex der inneren Schleife (N-1) ist nach jedem
		   * Durchlauf der äußeren Schhleife kleiner, weil n nach jedem Durchlauf der
		   * äußeren Schleife um1 kleiner wird.
		   * 
		   * 
		   */
	    for (int i=0; i<n-1; i=i+1)
	    {
	      if (a[i] > a[i+1])
	      {
	    	  /**
	    	   * SWAP a[i], a[i+1]
	    	   * 
	    	   * Wenn für zwei Nachbarwerte des Arrays die Reihenfolge nicht stimmt (siehe
	    	   * Bedingung im Kopf des if-Blocks),
	    	   * dann werden die zwei Werte gegeneinander ausgetauscht.
	    	   */
	        b=a[i]; // der Wert an der i-ten Stelle ist in b zwischengespeiichert.
	        a[i]=a[i+1];  // die Werte an der i-ten und an der (i+1)-ten Stelle wurden
	                      // gleichgesetzt.
	        a[i+1]=b; // der zwiischengespeicherter ursprünglicher Wert von a[i]
	                  // wird nach der (i+1)-ten Stelle übertragen.
	        /**
	         * Jetzt der Wert a[i] in a[i+1], und der ursprünglicher Wert von a[i+1]
	         * in a[i]. 
	         */
	      } // ende if
	    } // ende innere for-Schleife
	  } // ende äußere for-Schleife
	}
}

