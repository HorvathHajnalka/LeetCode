class RecursionExamples{
    public static void main(String [] args){

    }
    //fibonacci recursion - O(2^n)
    int fibonacci(int i) {
        if (i == 0) return 0;
        if (i == 1) return 1;
        return fibonacci(i - 1) + fibonacci(i - 2);
        }

    //optimized - O(n)
    int fibonacci2(int n) {
        return fibonacci2(n, new int[n + 1]);
    }
    int fibonacci2(int i, int[] memo) {
        if (i == 0 || i == 1) return i;
        if (memo[i] == 0) {
            memo[i] = fibonacci2(i - 1, memo)+ fibonacci2(i - 2, memo);
        }
        return memo[i];
        } 
}