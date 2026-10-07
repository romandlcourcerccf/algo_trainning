#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <numeric>
#include <ranges>
#include <string>
#include <vector>

class Solution {
 public:
  std::string getSolution(std::vector<std::string> map) {
    int stairs = std::stoi(map[0]);
    std::vector<int> dp(stairs + 1, 0);

    dp[0] = 1;
    dp[1] = 1;

    for (int i = 2; i < stairs + 1; i++) {
      if (i == 2) {
        dp[i] = dp[i - 1] + dp[i - 2];
      } else if (i > 2) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
      }
    }

    std::string res = std::to_string(dp.back());
    return res;
    }
};

int main() {
  std::string row;
  std::cin >> row;
  std::vector<std::string> input;
  input.push_back(row);

  Solution solution;
  std::string result = solution.getSolution(input);

  std::cout << result << std::endl;

  return 0;
}