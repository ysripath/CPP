class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum = 0;
        auto itr = nums.begin();
        while (itr != nums.end()) {
            sum += *itr;
            itr++;
        }
        
        int lSum = 0;
        
        int l = nums.size();
       
        for (int i = 0; i < l; i++) 
        {
            sum -= nums[i];
            if (sum == lSum)
                return i;
            lSum += nums[i];
        }
        return -1;
    }
};
