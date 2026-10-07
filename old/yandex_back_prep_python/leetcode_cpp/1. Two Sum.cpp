#include <map>
#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    std::unordered_map<int, int> s;

    for (int i = 0; i < nums.size(); i++) {
      if (s.contains(target - nums[i])) {
        return std::vector<int>{i, s[target - nums[i]]};
      }
      s[nums[i]] = i;
    }

    return std::vector<int>{};
  }
};