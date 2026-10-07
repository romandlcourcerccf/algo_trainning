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
  static vector<string>* read(string path) {
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

class Parser {
 public:
  static std::vector<std::string>* parse(std::string& str) {
    std::stringstream ss(str);
    std::vector<std::string>* integers = new std::vector<std::string>();

    std::string row;
    while (ss >> row) {
      integers->push_back(row);
    }
    return integers;
  }
};

class Transformer {
 public:
  static std::vector<int>* to_int(vector<std::string>& strings) {
    std::vector<int>* res = new std::vector<int>();

    for (std::string str : strings) {
      res->push_back(std::stoi(str));
    }

    return res;
  }
};

class Smoother {
 public:
  static std::vector<int>* smooth(std::vector<int>& array, int win_size) {
    // std::priority_queue<int> min_heap_right;
    // std::priority_queue<int, std::vector<int>, std::greater<int>>
    // max_heap_left;

    std::vector<int>* res = new std::vector<int>();

    for (int i = 0; i < array.size() + 1; i++) {
      std::vector<int> w;
      for (int j = 0; j < i; j++) {
        w.push_back(array[j]);
      }

      std::sort(w.begin(), w.end());

      if (w.size() > 0) {
        if (w.size() % 2 != 0) {
          res->push_back(w[(w.size()) / 2]);
        } else {
          res->push_back(w[(w.size() - 1) / 2]);
        }
      }
    }

    return res;
  }
};

int main() {
  vector<std::string>* rows = FileReader::read("2.txt");
  std::vector<std::string>* strings = Parser::parse((*rows)[1]);
  std::vector<int>* integers = Transformer::to_int(*strings);

  std::vector<int>* mediana =
      Smoother::smooth(*(integers), std::stoi((*rows)[0]));

  for (int i : (*mediana)) {
    std::cout << i << " ";
  }
  std::cout << std::endl;

  delete strings;
  delete rows;

  return 0;
}
