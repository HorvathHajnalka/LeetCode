public class SortingAlgorithms {
    // Mergesort algoritmus
    public static void mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return; // Ha az array egy vagy üres, nincs teendő
        }

        // A tömb felezése
        int mid = arr.length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.length - mid];

        // Az eredeti tömb felosztása bal és jobb részre
        for (int i = 0; i < mid; i++) {
            left[i] = arr[i];
        }
        for (int i = mid; i < arr.length; i++) {
            right[i - mid] = arr[i];
        }

        // A bal és jobb részt külön-külön sorba rendezzük
        mergeSort(left);
        mergeSort(right);

        // A rendezett bal és jobb részek összefésülése
        merge(arr, left, right);
    }

    // Két rendezett tömb összefésülése
    private static void merge(int[] arr, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;

        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }

        while (i < left.length) {
            arr[k++] = left[i++];
        }

        while (j < right.length) {
            arr[k++] = right[j++];
        }
    }

    // Quicksort algoritmus
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // Pivot = felosztóelem kiválasztása és annak indexének visszaadása
            int pivotIndex = partition(arr, low, high);

            // A pivot körül lévő részek rekurzívan rendezése
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    // Pivot elem kiválasztása és a tömb részekre osztása
    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};
        
        // Mergesort hívása
        mergeSort(arr);
        System.out.println("Mergesort rendezés:");
        for (int num : arr) {
            System.out.print(num + " ");
        }

        // Quicksort hívása
        int[] arr2 = {12, 11, 13, 5, 6};
        quickSort(arr2, 0, arr2.length - 1);
        System.out.println("\nQuicksort rendezés:");
        for (int num : arr2) {
            System.out.print(num + " ");
        }
    }
}
