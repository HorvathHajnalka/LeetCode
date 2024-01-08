//not mentioned in book 
class TreeDeleteInsertExamples{
    class TreeNode {
        int value;
        TreeNode left;
        TreeNode right;

        public TreeNode(int value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }

    public class BinarySearchTree {
        private TreeNode root;

        public BinarySearchTree() {
            root = null;
        }

        // Beszúrás egy értéket a bináris kereső fába
        public void insert(int value) {
            root = insertRec(root, value);
        }

        // Rekurzív beszúró metódus
        private TreeNode insertRec(TreeNode root, int value) {
            if (root == null) {
                root = new TreeNode(value);
                return root;
            }

            if (value < root.value) {
                root.left = insertRec(root.left, value);
            } else if (value > root.value) {
                root.right = insertRec(root.right, value);
            }

            return root;
        }

        // Törlés egy értéket a bináris kereső fából
        public void delete(int value) {
            root = deleteRec(root, value);
        }

        // Rekurzív törlő metódus
        private TreeNode deleteRec(TreeNode root, int value) {
            if (root == null) {
                return root;
            }

            if (value < root.value) {
                root.left = deleteRec(root.left, value);
            } else if (value > root.value) {
                root.right = deleteRec(root.right, value);
            } else {
                if (root.left == null) {
                    return root.right;
                } else if (root.right == null) {
                    return root.left;
                }

                root.value = minValue(root.right);
                root.right = deleteRec(root.right, root.value);
            }

            return root;
        }

        // Segédmetódus a minimális érték kereséséhez a jobb részfában
        private int minValue(TreeNode node) {
            int minValue = node.value;
            while (node.left != null) {
                minValue = node.left.value;
                node = node.left;
            }
            return minValue;
        }
    }
    public static void main(String[] args) {
        // Bináris kereső fa létrehozása
        BinarySearchTree bst = new BinarySearchTree();

        // Értékek beszúrása a fába
        bst.insert(50);
        bst.insert(30);
        bst.insert(20);
        bst.insert(40);
        bst.insert(70);
        bst.insert(60);
        bst.insert(80);


        // Érték törlése a fából
        int valueToDelete = 30;
        System.out.println("\nTörlés az értékkel " + valueToDelete);
        bst.delete(valueToDelete);

    }
}