class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int s = nums.size();
        
        
        int val1 = 0;
        int val2 = 0;
        int count = 1;
        auto itr = nums.begin();
        while (itr != nums.end()) {
            val1 ^= *itr;
            itr++;
            val2 ^= count++;
        }
        return (val1^val2);
    }
};
