import java.util.Hashtable;

public class HashTableExample {
    public static void main(String[] args) {
        // Hashtable létrehozása és inicializálása
        Hashtable<Integer, String> hashtable = new Hashtable<>();

        // Elemek hozzáadása a Hashtable-hez
        hashtable.put(1, "Első elem");
        hashtable.put(2, "Második elem");
        hashtable.put(3, "Harmadik elem");

        // Elemek lekérdezése a kulcs alapján O(1)
        String value = hashtable.get(2);
        System.out.println("A kulcs 2-hez tartozó érték: " + value);

        // Kulcs-érték párok kiíratása
        System.out.println("Kulcs-érték párok:");
        for (Integer key : hashtable.keySet()) {
            String val = hashtable.get(key);
            System.out.println(key + " -> " + val);
        }

        // Kulcs alapján történő törlés
        hashtable.remove(1);

        // Ellenőrzés, hogy egy kulcs létezik-e a Hashtable-ben
        boolean containsKey = hashtable.containsKey(3);
        System.out.println("A kulcs 3 létezik-e? " + containsKey);

        // Ellenőrzés, hogy egy érték létezik-e a Hashtable-ben
        boolean containsValue = hashtable.containsValue("Negyedik elem");
        System.out.println("A 'Negyedik elem' létezik-e? " + containsValue);
    }
}