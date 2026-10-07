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
    std::priority_queue<int> min_heap_right;
    std::priority_queue<int, std::vector<int>, std::greater<int>> max_heap_left;

    for (int i = 0; i < array.size() - win_size; i++) {
      if (i == 0) {
        for (int j = 0; j < win_size; j++) {
          if (max_heap_left.size() == min_heap_right.size()) {
              min_heap_right.push(array[j]); 
          } else if (max_heap_left.size() < min_heap_right.size()) {
              
          }
        }
      }
    }
  }
};

int main() {
  vector<std::string>* rows = FileReader::read("1.txt");
  std::vector<std::string>* strings = Parser::parse((*rows)[1]);
  std::vector<int>* integers = Transformer::to_int(*strings);

  for (int i : *(integers)) {
    std::cout << ">>" << i << std::endl;
  }

  delete strings;
  delete rows;

  return 0;
}
