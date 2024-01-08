import java.util.ArrayList;
import java.util.Collections; //sort()-hoz

public class ArrayListExample {
    public static void main(String[] args) {
        // ArrayList létrehozása és inicializálása
        ArrayList<String> arrayList = new ArrayList<>();
        ArrayList<Integer> numbers = new ArrayList<>();

        // Elemek hozzáadása az ArrayList-hez O(1)
        arrayList.add("Első elem");
        arrayList.add("Második elem");
        arrayList.add("Harmadik elem");

        // Elemek lekérdezése a pozíció alapján
        String element = arrayList.get(1);
        System.out.println("Az index 1-hez tartozó elem: " + element);

        // ArrayList elemeinek kiíratása
        System.out.println("ArrayList elemei:");
        for (String item : arrayList) {
            System.out.println(item);
        }

        // Elemek eltávolítása
        arrayList.remove(0);

        // Ellenőrzés, hogy egy elem szerepel-e az ArrayList-ben
        boolean contains = arrayList.contains("Negyedik elem");
        System.out.println("A 'Negyedik elem' szerepel-e? " + contains);

        // ArrayList elemeinek rendezése - "mergesort" és az "insertion sort" algoritmusok egy kombinációja- O(n log n)
        //növekvő
        Collections.sort(numbers);
        //csökkenő
        Collections.sort(numbers, Collections.reverseOrder());
    }
}
