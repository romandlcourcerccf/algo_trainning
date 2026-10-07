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

class Heap {
 public:
  int top(void) {
    int res = this->heap[0];
    this->heap.pop_front();
    if (this->heap.size() == 0) {
      return res;
    }

    this->swap(0, this->heap.size() - 1);

    if (this->heap.size() > 1) {
      this->pop_down();
    }
    return res;
  }
  void add(int val) {
    this->heap.push_back(val);
    this->pop_up();
  }

 private:
  std::deque<int> heap;
  void pop_up(void) {
    int i = this->heap.size() - 1;
    while (i != 0) {
      int p = (i - 1) / 2;  // remember this
      if (this->heap[p] <= this->heap[i]) {
        this->swap(p, i);
      }
      i = p;
    }
  }
  void pop_down(void) {
    int i = 0;
    int l_child = (2 * i) + 1;  // remember this
    int r_child = (2 * i) + 2;  // remember this
    int h_len = this->heap.size();
    if (l_child < h_len && r_child < h_len) {
      int min_child = -1;
      if (this->heap[l_child] > this->heap[r_child]) {
        min_child = l_child;
      } else {
        min_child = r_child;
      }
      if (this->heap[i] < this->heap[min_child]) {
        this->swap(i, min_child);
      }
    } else if (l_child < h_len) {
      if (this->heap[i] <= this->heap[l_child]) {
        this->swap(i, l_child);
      }
    } else if (r_child < h_len) {
      if (this->heap[i] <= this->heap[r_child]) {
        this->swap(i, r_child);
      }
    }
  }

  void swap(int i, int j) {
    int tmp = this->heap[i];
    this->heap[i] = this->heap[j];
    this->heap[j] = tmp;
  }
};

int main() {
  FileReader reader;
  Heap heap;
  vector<std::string>* rows = reader.read("1.txt");

  for (int i = 1; i < (*rows).size(); i++) {
    vector<std::string>* parsed_row = Parser::parse((*rows)[i]);
    if ((*parsed_row)[0] == "0") {
      int el = std::stoi((*parsed_row)[1]);
      heap.add(el);
    } else {
      std::cout << heap.top() << std::endl;
    }
  }

  delete rows;

  return 0;
}
