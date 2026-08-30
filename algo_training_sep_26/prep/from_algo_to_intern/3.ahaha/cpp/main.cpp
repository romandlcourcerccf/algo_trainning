#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> read_lines(std::string& path) {
  std::fstream fs(path);
  std::vector<std::string> result;
  std::string row;

  while (std::getline(fs, row)) {
    result.push_back(row);
  }

  fs.close();

  return result;
}

int main() {
  std::string path = "test_4.txt";
  std::vector<std::string> rows = read_lines(path);

  std::string row = rows[1];
  std::cout << row << std::endl;

  int row_len = std::stoi(rows[1]);

  int l = 0;
  int r = 0;
  int max_len = 0;

  std::cout << "row_len :" << row_len << std::endl;

  while (r < row.size()) {
    std::cout << "r" << r << std::endl;

    if ((row[r] == 'a' && row[r + 1] == 'h') ||
        (row[r] == 'h' && row[r + 1] == 'a')) {
      max_len = std::max(max_len, r - l + 1);
    } else {
      l = r;
    }

    r++;
  }

  std::cout << "max_len :" << max_len << std::endl;

  return 0;
}
