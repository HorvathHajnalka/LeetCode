import java.util.ArrayList;
public class BinaryMinHeap {
    private ArrayList<Integer> heap;

    public BinaryMinHeap() {
        this.heap = new ArrayList<>();
    }

    public void insert(int value) {
        // Az új elemet a kupac végére hozzuk létre
        heap.add(value);

        // A kupacot újra rendezzük a minimum kupac tulajdonságok megtartása érdekében
        heapifyUp(heap.size() - 1);
    }

    private void heapifyUp(int index) {
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            if (heap.get(index) < heap.get(parentIndex)) {
                // Ha az aktuális elem kisebb a szülőnél, cseréljük meg őket
                int temp = heap.get(index);
                heap.set(index, heap.get(parentIndex));
                heap.set(parentIndex, temp);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    public int extractMin() {
        if (heap.isEmpty()) {
            throw new IllegalStateException("A kupac üres.");
        }

        int minValue = heap.get(0);

        // Az utolsó elemet helyezzük a gyökér pozíciójába
        int lastIndex = heap.size() - 1;
        heap.set(0, heap.get(lastIndex));
        heap.remove(lastIndex);

        // A kupacot újra rendezzük a minimum kupac tulajdonságok megtartása érdekében
        heapifyDown(0);

        return minValue;
    }

    private void heapifyDown(int index) {
        int leftChild = 2 * index + 1;
        int rightChild = 2 * index + 2;
        int smallest = index;

        if (leftChild < heap.size() && heap.get(leftChild) < heap.get(smallest)) {
            smallest = leftChild;
        }

        if (rightChild < heap.size() && heap.get(rightChild) < heap.get(smallest)) {
            smallest = rightChild;
        }

        if (smallest != index) {
            // Ha a legkisebb érték nem a jelenlegi csomópont, cseréljük meg őket
            int temp = heap.get(index);
            heap.set(index, heap.get(smallest));
            heap.set(smallest, temp);
            heapifyDown(smallest);
        }
    }

    public boolean isEmpty() {
        return heap.isEmpty();
    }

    public void printHeap() {
        for (int value : heap) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        BinaryMinHeap minHeap = new BinaryMinHeap();

        minHeap.insert(10);
        minHeap.insert(8);
        minHeap.insert(12);
        minHeap.insert(4);
        minHeap.insert(6);

        System.out.println("A minimum kupac tartalma:");
        minHeap.printHeap();

        int minValue = minHeap.extractMin();
        System.out.println("Kivett minimális érték: " + minValue);

        System.out.println("A minimum kupac tartalma a kivétel után:");
        minHeap.printHeap();
    }  
}
