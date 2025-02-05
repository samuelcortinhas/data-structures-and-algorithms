// python ints are arbitrarily large so this algorithm doesn't work,
// whereas in java ints are 32 bits
class Solution {
    public int getSum(int a, int b) {
        // Time O(1), Memory O(1)
        while (b != 0) {
            int tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
}
