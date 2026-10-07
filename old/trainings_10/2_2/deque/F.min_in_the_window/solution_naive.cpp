#include <algorithm>
#include <deque>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

std::vector<int> parse(std::string& str) {
  std::stringstream ss(str);
  std::vector<int> integers;

  std::string row;
  while (ss >> row) {
    integers.push_back(std::stoi(row));
  }
  return integers;
}

class FileReader {
 public:
  vector<string>* read(string path) {
    vector<string>* rows = new vector<string>();

    std::fstream file(path);

    std::string row;

    while (std::getline(file, row)) {
      rows->push_back(row);
    }

    file.close();

    return rows;
  }
};

int main() {
  FileReader reader;
  vector<std::string>* rows = reader.read("input.txt");

  std::vector<int> params = parse(rows->at(0));
  std::vector<int> array = parse(rows->at(1));

  int array_len = params[0];
  int win_size = params[1];

  std::cout << "array_len :" << array_len << "win_size :" << win_size
            << std::endl;

  // 1 3 2 4 5 3 1

  for (int i = 0; i < array_len - win_size + 1; i++) {
    int min = std::numeric_limits<int>::max();

    for (int k = i; k < i + win_size; k++) {
      min = std::min(min, array[k]);
    }

    std::cout << "max :" << min << std::endl;
  }

  return 0;
}
