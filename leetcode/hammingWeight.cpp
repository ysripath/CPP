class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        int k = 32;
        while (k--) {
            count += (n&1)?1:0;
            n=n>>1;
        }
        return count;
    }
};
