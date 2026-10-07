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
  std::string getSolution(std::string str) {
    std::map<char, int> scores;
    std::map<int, char> scores_rev;

    auto range = std::views::iota('A', 'Z' + 1) | std::views::reverse;

    for (int i = 0; i < range.size(); i++) {
      scores[range[i]] = i;
      scores_rev[i] = range[i];
    }

    std::vector<int> scores_vector;

    for (char c : str) {
      scores_vector.push_back(scores[c]);
    }

    int min_score =
        *std::min_element(scores_vector.begin(), scores_vector.end());

    std::cout << "min_score :" << min_score << std::endl;

    int sum_of_scores =
        std::accumulate(scores_vector.begin(), scores_vector.end(), 0);

    int average_score = std::ceil(sum_of_scores / scores_vector.size());

    std::cout << "average_score :" << average_score << std::endl;

    if (std::abs(average_score - min_score) > 1) {
      average_score = min_score + 1;
    }

    std::cout << "res : " << scores_rev[average_score] << std::endl;

    std::string res(1, scores_rev[average_score]);
    return res;
  }
};
