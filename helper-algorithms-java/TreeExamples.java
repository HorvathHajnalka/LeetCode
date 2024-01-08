public class TreeTravelsarExamples {
    //létrehozás
    static class TreeNode {
        public int value;
        public TreeNode left;
        public TreeNode right;
        
        public TreeNode(int value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }

    public static void main(String[] args) {
        // Példa bináris kereső fa létrehozása
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(3);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(7);
        root.right.right = new TreeNode(9);

        // In-order bejárás elindítása
        inOrderTraversal(root);
        // Pre-order bejárás elindítása
        preOrderTraversal(root);
        // Post-order bejárás elindítása
        postOrderTraversal(root);
    }

    // In-order bejárás
    static void inOrderTraversal(TreeNode node) {
        if (node != null) {
            // Először megyünk balra (kisebb értékek)
            inOrderTraversal(node.left);
            // Csomópont meglátogatása (jelen esetben csak kiírjuk az értéket)
            System.out.println(node.value);
            // Majd megyünk jobbra (nagyobb értékek)
            inOrderTraversal(node.right);
        }
    }
    //Pre-order bejárás
    static void preOrderTraversal(TreeNode node) {
        if (node != null) {
            // Csomópont meglátogatása (jelen esetben csak kiírjuk az értéket)
            System.out.println(node.value);
            // Először megyünk balra (kisebb értékek)
            preOrderTraversal(node.left); 
            // Majd megyünk jobbra (nagyobb értékek)
            preOrderTraversal(node.right);
        }
    }
    // Post-order bejárás bináris kereső fában
    static void postOrderTraversal(TreeNode node) {
        if (node != null) {
            // Először megyünk balra (kisebb értékek)
            postOrderTraversal(node.left);
            // Majd megyünk jobbra (nagyobb értékek)
            postOrderTraversal(node.right);
            // Csomópont meglátogatása (jelen esetben csak kiírjuk az értéket)
            System.out.println(node.value);
        }
    }
}