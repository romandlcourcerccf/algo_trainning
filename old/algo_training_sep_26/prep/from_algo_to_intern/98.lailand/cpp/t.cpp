#include <iostream>
#include <map>
#include <ranges>
#include <string>

int main() {
  std::map<char, int> scores;
  std::string s = "AZ";

  auto range = std::views::iota('A', 'Z' + 1) | std::views::reverse;

  std::cout << ">>" << range.size() << std::endl;

  for (int i = 0; i < range.size(); i++) {
    std::cout << range[i] << std::endl;
    scores[range[i]] = i;
  }

  std::cout << ">>" << scores['J'] << std::endl;

  return 0;
}