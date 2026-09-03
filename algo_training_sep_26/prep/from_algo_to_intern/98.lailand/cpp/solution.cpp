#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <ranges>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

class Solution {
 private:
  std::vector<int> parse(std::string& str) {
    std::stringstream ss(str);
    std::vector<int> integers;

    int temp;
    while (ss >> temp) {
      integers.push_back(temp);
    }
    return integers;
  }

  std::string to_string(std::vector<int>& v) {
    std::string res("");
    for (int i = 0; i < v.size(); i++) {
      res += std::to_string(v[i]);
      if (i < v.size() - 1) {
        res += ' ';
      }
    }
    return res;
  }

 public:
  std::string getSolution(std::vector<std::string>& input) {
    std::string size = input[0];
    std::string cities = input[1];

    std::vector<int> cities_vector = this->parse(cities);
    std::vector<int> dp(cities_vector.size(), -1);
    std::stack<std::pair<int, int>> stack;

    for (int i = 0; i < cities_vector.size(); i++) {
      while (!stack.empty() and stack.top().second > cities_vector[i]) {
        dp[stack.top().first] = i;
        stack.pop();
      }
      stack.push(std::make_pair(i, cities_vector[i]));
    }

    return this->to_string(dp);
  }
};

std::vector<std::string> get_rows(void) {
  std::vector<std::string> res;
  std::ifstream file("input.txt");
  std::string row;

  while (std::getline(file, row)) {
    res.push_back(row);
  }

  file.close();

  return res;
}

int main() {
  std::vector<std::string> rows = get_rows();
  Solution solution;
  std::string result = solution.getSolution(rows);
  std::cout << result << std::endl;
  return 0;
}
