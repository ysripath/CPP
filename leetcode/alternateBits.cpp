class Solution {
public:
    bool hasAlternatingBits(int n) {
      
        int i = 0;
        int k = 1;
        while (n) {
            if (((n>>i)&1) == ((n>>k)&1))
            {
                return false;
            }
            n >>= 1;
        }
        return true;
    }
};
