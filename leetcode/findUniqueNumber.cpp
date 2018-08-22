class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int val1 = 0;
        
        auto itr = nums.begin();
        
        while (itr != nums.end())
        {
            val1 ^= *itr;
            itr++;
        }
        
        return val1;
    }
};
