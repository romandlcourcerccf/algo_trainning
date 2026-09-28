#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <list>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

std::vector<std::string> parse(std::string& str) {
  std::stringstream ss(str);
  std::vector<string> integers;

  std::string row;
  while (ss >> row) {
    integers.push_back(row);
  }
  return integers;
}

class ProtectedQueue {
 public:
  ProtectedQueue(void) { this->operations = new list<int>(); }
  ~ProtectedQueue() { delete this->operations; }

  void push(int n) {
    operations->push_back(n);
    std::cout << "ok" << std::endl;
  }

  void pop(void) {
    if (this->operations->size() == 0) {
      std::cout << "error" << std::endl;
      return;
    }

    std::cout << this->operations->front() << std::endl;
    operations->pop_front();
  }

  void front(void) {
    if (this->operations->size() == 0) {
      std::cout << "error" << std::endl;
      return;
    }

    std::cout << this->operations->front() << std::endl;
  }

  void size(void) { std::cout << this->operations->size() << std::endl; }

  void clear(void) {
    this->operations->clear();
    std::cout << "ok" << std::endl;
  }

 private:
  std::list<int>* operations;
};

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
  ProtectedQueue queue;

  vector<string>* rows = reader.read("2.txt");

  for (std::string command : *rows) {
    if (command == "exit") {
      std::cout << "bye" << std::endl;
      return 0;
    }

    std::vector<std::string> operands = parse(command);

    if (operands[0] == "pop") {
      queue.pop();

    } else if (operands[0] == "push") {
      queue.push(std::stoi(operands[1]));
    } else if (operands[0] == "front") {
      queue.front();
    } else if (operands[0] == "clear") {
      queue.clear();
    } else if (operands[0] == "size") {
      queue.size();
    }
  }

  return 0;
}
