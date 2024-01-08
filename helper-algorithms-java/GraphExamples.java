//The Graph class is used because, unlike in a tree, you can't necessarily reach all the nodes from a single node.
class GraphExamples{
    class Graph {
        public Node[] nodes;
    }

    class Node {
        public String name;
        public Node[] children;
    }
}

