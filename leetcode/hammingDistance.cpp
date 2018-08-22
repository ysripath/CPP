class Solution {
public:
    int hammingDistance(int x, int y) {
        x ^= y;
        int count = 0;
        for (int i = 0; i<32; i++){
            (x&1)==1?count++:count;
            x=x>>1;
        }
        return count;
    }
};
