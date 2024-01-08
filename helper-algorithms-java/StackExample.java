import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        // Stack létrehozása
        Stack<Integer> stack = new Stack<>();

        // Elemek hozzáadása a veremhez (push)
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);

        // Ellenőrzés, hogy a verem üres-e (isEmpty)
        boolean isEmpty = stack.isEmpty();
        System.out.println("A verem üres? " + isEmpty);

        // A verem tetején lévő elem lekérése (peek)
        int topElement = stack.peek();
        System.out.println("A verem tetején lévő elem: " + topElement);

        // Elem eltávolítása a veremből (pop) -- eltárolhatjuk
        int poppedElement = stack.pop();
        System.out.println("Az eltávolított elem: " + poppedElement);

        // A verem kiürítése
        stack.clear();

        // Ellenőrzés, hogy a verem üres-e újra
        isEmpty = stack.isEmpty();
        System.out.println("A verem újra üres? " + isEmpty);
    }
}