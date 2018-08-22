class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t r = 0;
        int k = 32;
        while (k--) {
            r<<=1;
            if (n&1)
                r ^= 1;
            n>>=1;
        }
        return r;
    }
};
