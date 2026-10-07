#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include "algo.cpp"

using namespace std;

std::vector<std::string> split_row(const std::string& str) {
  std::vector<std::string> result;

  std::stringstream ss(str);
  std::string word;

  while (ss >> word) {
    result.push_back(word);
  }

  return result;
}

std::vector<char> split_row_to_chars(const std::string& str) {
  std::vector<char> result;

  for (char c : str) {
    result.push_back(c);
  }

  return result;
}

std::vector<std::vector<char>> readRows(std::string path) {
  std::fstream fs(path);
  std::vector<std::vector<char>> result;

  std::string row;

  while (std::getline(fs, row)) {
    result.push_back(split_row_to_chars(row));
  }

  fs.close();

  return result;
}

void print(std::vector<std::vector<std::string>> rows) {
  for (std::vector<std::string> row : rows) {
    for (std::string s : row) {
      std::cout << s << " ";
    }
    std::cout << std::endl;
  }
}

void print(std::vector<std::vector<char>> rows) {
  for (std::vector<char> row : rows) {
    for (char s : row) {
      std::cout << s << " ";
    }
    std::cout << std::endl;
  }
}

int main() {
  Solution solution;

  std::vector<std::vector<char>> rows = readRows("test_1.txt");

  std::vector<std::vector<char>> maze =

      solution.nearestExit(maze);

  return 0;
}

// include <iostream>
// #include <vector>
// #include <algorithm>
// #include <iterator>

// int main() {
//     std::vector<int> src = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
//     std::vector<int> dest;

//     // C++20 Ranges syntax
//     std::ranges::copy_if(src, std::back_inserter(dest), [](int x) {
//         return x % 2 == 0;
//     });
// }