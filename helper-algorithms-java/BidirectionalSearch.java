import java.util.*;

public class BidirectionalSearch {
    class Node {
        int data;
        boolean marked;
        List<Node> adjacent;

        Node(int data) {
            this.data = data;
            this.marked = false;
            this.adjacent = new ArrayList<>();
        }
    }

    public boolean bidirectionalSearch(Node start, Node end) {
        Set<Node> startSet = new HashSet<>();
        Set<Node> endSet = new HashSet<>();

        Queue<Node> startQueue = new LinkedList<>();
        Queue<Node> endQueue = new LinkedList<>();

        startSet.add(start);
        endSet.add(end);

        startQueue.add(start);
        endQueue.add(end);

        while (!startQueue.isEmpty() && !endQueue.isEmpty()) {
            if (hasIntersection(startSet, endSet)) {
                return true; // A találat történt, megtaláltuk a célt
            }

            searchLevel(startQueue, startSet);
            searchLevel(endQueue, endSet);
        }

        return false; // Nem találtuk meg a célt
    }

    private boolean hasIntersection(Set<Node> set1, Set<Node> set2) {
        for (Node node : set1) {
            if (set2.contains(node)) {
                return true;
            }
        }
        return false;
    }

    private void searchLevel(Queue<Node> queue, Set<Node> set) {
        int levelSize = queue.size();
        for (int i = 0; i < levelSize; i++) {
            Node node = queue.poll();
            for (Node neighbor : node.adjacent) {
                if (!set.contains(neighbor)) {
                    set.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }
    }

    public static void main(String[] args) {
        BidirectionalSearch search = new BidirectionalSearch();

        Node node1 = search.new Node(1);
        Node node2 = search.new Node(2);
        Node node3 = search.new Node(3);
        Node node4 = search.new Node(4);
        Node node5 = search.new Node(5);

        node1.adjacent.add(node2);
        node1.adjacent.add(node3);
        node2.adjacent.add(node4);
        node3.adjacent.add(node5);

        // Bidirekcionális keresés
        Node startNode = node1;
        Node endNode = node5;
        boolean found = search.bidirectionalSearch(startNode, endNode);
        if (found) {
            System.out.println("Bidirekcionális keresés: Megtaláltuk a célt.");
        } else {
            System.out.println("Bidirekcionális keresés: Nincs találat.");
        }
    }
}
