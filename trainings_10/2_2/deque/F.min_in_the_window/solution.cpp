#include <algorithm>
#include <deque>
#include <fstream>
#include <iostream>
#include <iterator>
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

  std::deque<int> window;

  for (int i = 0; i < array_len - win_size + 1; i++) {
    for (int k = i; k < i + win_size; k++) {
      while (!window.empty() && window.back() >= array[k]) {
        window.pop_back();
      }
      window.push_back(array[k]);
    }

    if (i > 0) {
      if (!window.empty() && array[i - 1] == window.front()) {
        window.pop_front();
      }
    }

    std::cout << window.front() << std::endl;
  }

  return 0;
}
