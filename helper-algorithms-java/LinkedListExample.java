public class LinkedListExample {

    // Belső osztály a láncolt lista csomópontjainak reprezentálásához
    private static class Node {
        int data; // Adat
        Node next; // Következő csomópont mutatója

        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node head; // Lista feje

    // Lista létrehozása üresen O(1)
    public LinkedListExample() {
        head = null;
    }

    // Elem hozzáadása a lista végéhez O(1)
    public void append(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }

        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }

    // Elem beszúrása a lista elejére O(1)
    public void prepend(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    // Elem törlése a listából O(n)
    public void delete(int data) {
        if (head == null) {
            return;
        }

        if (head.data == data) {
            head = head.next;
            return;
        }

        Node current = head;
        while (current.next != null) {
            if (current.next.data == data) {
                current.next = current.next.next;
                return;
            }
            current = current.next;
        }
    }

    // Lista kiíratása
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        LinkedListExample list = new LinkedListExample();

        list.append(1);
        list.append(2);
        list.append(3);

        System.out.println("Eredeti lista:");
        list.printList();

        list.prepend(0);
        System.out.println("Lista elejére beszúrás után:");
        list.printList();

        list.delete(2);
        System.out.println("Elem törlése után:");
        list.printList();
    }
}
