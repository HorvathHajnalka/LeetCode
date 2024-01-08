public class BinarySearchExample {

    // Bináris keresés algoritmus (rekurzív megvalósítás)
    public static int binarySearch(int[] arr, int low, int high, int target) {
        if (low <= high) {
            int mid = low + (high - low) / 2;

            // Ha a középső elem a keresett elem
            if (arr[mid] == target) {
                return mid;
            }

            // Ha a keresett elem a bal részben van
            if (arr[mid] > target) {
                return binarySearch(arr, low, mid - 1, target);
            }

            // Ha a keresett elem a jobb részben van
            return binarySearch(arr, mid + 1, high, target);
        }

        // Ha a keresett elem nem található az array-ben
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};

        // Bináris keresés példa
        int target = 2;
        int result = binarySearch(arr, 0, arr.length - 1, target);
        if (result == -1) {
            System.out.println("A keresett elem nem található az array-ben.");
        } else {
            System.out.println("A keresett elem indexe: " + result);
        }
    }
}
