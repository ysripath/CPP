class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        
        int SUM = 0;
        int minDiff = 999999;
        int sum;
        int i = 0;
        int k = nums.size()-1;
        int j = i+1;
        
        for (i = 0; i < nums.size() - 2; i++)
        {
            k = nums.size()-1;
            j = i+1;
            sum = nums[i] + nums[j] + nums[k];
            
            if (sum == target)
                return target;
            while (j < k)
            {
                if (sum == target)
                    return target;
                if (abs(target-sum) < minDiff)
                {
                    SUM = sum;
                    minDiff = abs(target-sum);
                }
                if (sum < target)
                {
                    j++;
                }
                else if ( sum > target)
                {
                    k--;
                }
                sum = nums[i] + nums[j] + nums[k];           
            }
        }
        sum = nums[i-1] + nums[i] + nums[i+1];
        if (sum == target)
            return target;
        else if (abs(target-sum) < minDiff)
            return sum;
        else
            return SUM;
    }
};
