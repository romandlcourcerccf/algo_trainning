#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <numeric>
#include <ranges>
#include <stack>
#include <string>
#include <vector>

class Solution {
 public:
  std::string getSolution(std::vector<std::string> input) {
    std::string par = input[0];

    std::stack<std::string> st;

    std::vector<std::string> pairs = {"[]", "{}", "()"};
    std::vector<std::string> left = {"[", "{", "("};

    for (char c : par) {
      std::string _c(1, c);

      if (std::find(left.begin(), left.end(), _c) != left.end()) {
        // if (std::ranges::contains(left, _c)) {
        st.push(_c);
      } else {
        if (st.size() == 0) {
          return "no";
        }

        std::string __c = st.top();
        st.pop();

        if (!(std::find(pairs.begin(), pairs.end(), __c + _c) != pairs.end())) {
          // if (!std::ranges::contains(pairs, __c + _c)) {
          return "no";
        }
      }
    }

    if (st.size() == 0) {
      return "yes";
    }

    return "no";
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
