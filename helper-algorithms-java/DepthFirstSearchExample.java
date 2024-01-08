import java.util.*;

public class DepthFirstSearchExample {
    class Graph {
        private int V; // A gráf csomópontjainak száma
        private LinkedList<Integer> adjList[]; // Szomszédsági listák

        public Graph(int v) {
            V = v;
            adjList = new LinkedList[v];
            for (int i = 0; i < v; i++) {
                adjList[i] = new LinkedList<>();
            }
        }

        // Él hozzáadása a gráfhoz
        public void addEdge(int v, int w) {
            adjList[v].add(w);
        }

        // Mélységi keresés a gráfban
        public void DFS(int v) {
            boolean visited[] = new boolean[V];
            DFSUtil(v, visited);
        }

        private void DFSUtil(int v, boolean visited[]) {
            visited[v] = true;
            System.out.print(v + " ");

            Iterator<Integer> iterator = adjList[v].listIterator();
            while (iterator.hasNext()) {
                int n = iterator.next();
                if (!visited[n]) {
                    DFSUtil(n, visited);
                }
            }
        }
    }

    public static void main(String[] args) {
        DepthFirstSearchExample dfsExample = new DepthFirstSearchExample();
        Graph g = dfsExample.new Graph(7); // Gráf létrehozása 7 csomóponttal

        // Élek hozzáadása a gráfhoz
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(1, 4);
        g.addEdge(2, 5);
        g.addEdge(2, 6);

        System.out.println("Mélységi keresés eredménye (kiinduló csomópont: 0):");
        g.DFS(0);
    }
}
