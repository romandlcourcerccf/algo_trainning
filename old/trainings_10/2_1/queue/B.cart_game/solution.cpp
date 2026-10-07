#include <algorithm>
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

std::list<int> parse(std::string& str) {
  std::stringstream ss(str);
  std::list<int> integers;

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
  vector<string>* rows = reader.read("1.txt");

  std::list<int> set_1 = parse(rows->at(0));
  std::list<int> set_2 = parse(rows->at(1));

  int counter = 0;
  while (!set_1.empty() && !set_2.empty()) {
    counter++;

    int card_1 = set_1.front();
    int card_2 = set_2.front();

    set_1.pop_front();
    set_2.pop_front();

    if ((card_1 == 0 && card_2 == 9) || (card_1 > card_2)) {
      set_1.push_back(card_1);
      set_1.push_back(card_2);
    } else {
      set_2.push_back(card_2);
      set_2.push_back(card_1);
    }
  }

  if (set_1.empty()) {
    std::cout << "second " << counter << std::endl;
    return 0;
  }

  if (set_2.empty()) {
    std::cout << "first" << counter << std::endl;
    return 0;
  }

  return 0;
}
