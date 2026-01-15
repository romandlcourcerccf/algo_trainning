class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map <int,int> h;

        for (int i=0; i < nums.size(); i++) {
            if (h.contains(target - nums[i])) {
                return vector<int>({i, h[target - nums[i]]});
            } else {
                h[nums[i]] = i;
            }
        }

        return {0,0};
        
    }
};