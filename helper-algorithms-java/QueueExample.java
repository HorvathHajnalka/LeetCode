import java.util.LinkedList;
import java.util.Queue;

public class QueueExample {
    public static void main(String[] args) {
        // Queue létrehozása
        Queue<String> queue = new LinkedList<>();

        // Elemek hozzáadása a sorhoz (offer)
        queue.offer("Első elem");
        queue.offer("Második elem");
        queue.offer("Harmadik elem");

        // Ellenőrzés, hogy a sor üres-e (isEmpty)
        boolean isEmpty = queue.isEmpty();
        System.out.println("A sor üres? " + isEmpty);

        // A sor elején lévő elem lekérése (peek)
        String frontElement = queue.peek();
        System.out.println("A sor elején lévő elem: " + frontElement);

        // Elem eltávolítása a sorból (poll)
        String removedElement = queue.poll();
        System.out.println("Az eltávolított elem: " + removedElement);

        // A sor kiürítése
        queue.clear();

        // Ellenőrzés, hogy a sor üres-e újra
        isEmpty = queue.isEmpty();
        System.out.println("A sor újra üres? " + isEmpty);
    }
}