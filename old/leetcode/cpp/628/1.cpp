class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());

        if (nums.at(nums.size()-1)*nums.at(nums.size()-2)*nums.at(nums.size()-3) >  nums.at(0)*nums.at(1)*nums.at(nums.size()-1)) {
            return nums.at(nums.size()-1)*nums.at(nums.size()-2)*nums.at(nums.size()-3);
        } else {
            return nums.at(0)*nums.at(1)*nums.at(nums.size()-1);
        }
    }
};