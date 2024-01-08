import java.util.*;

public class GraphSearchExamples {
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

    // DFS (Mélységi keresés)
    public void DFS(Node root) {
        if (root == null) return;

        System.out.println("DFS (Mélységi keresés):");

        // Mélységi keresés indítása
        DFSUtil(root);
    }

    private void DFSUtil(Node node) {
        if (node == null) return;

        node.marked = true;
        visit(node);

        // Rekurzív mélységi keresés a szomszédos csomópontokon
        for (Node n : node.adjacent) {
            if (!n.marked) {
                DFSUtil(n);
            }
        }
    }

    // BFS (Szélességi keresés)
    public void BFS(Node root) {
        if (root == null) return;

        System.out.println("BFS (Szélességi keresés):");

        Queue<Node> queue = new LinkedList<>();
        root.marked = true;
        queue.add(root);

        while (!queue.isEmpty()) {
            Node node = queue.poll();
            visit(node);

            // Szélességi keresés a szomszédos csomópontokon
            for (Node n : node.adjacent) {
                if (!n.marked) {
                    n.marked = true;
                    queue.add(n);
                }
            }
        }
    }

    private void visit(Node node) {
        System.out.print(node.data + " ");
    }

    public static void main(String[] args) {
        GraphSearchExamples searchExamples = new GraphSearchExamples();

        Node node1 = searchExamples.new Node(1);
        Node node2 = searchExamples.new Node(2);
        Node node3 = searchExamples.new Node(3);
        Node node4 = searchExamples.new Node(4);
        Node node5 = searchExamples.new Node(5);

        node1.adjacent.add(node2);
        node1.adjacent.add(node3);
        node2.adjacent.add(node4);
        node3.adjacent.add(node5);

        // Mélységi keresés (DFS)
        searchExamples.DFS(node1);
        System.out.println();

        // Szélességi keresés (BFS)
        searchExamples.BFS(node1);
    }
}
