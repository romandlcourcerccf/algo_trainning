#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "solution.cpp"

#include <string>
#include <vector>

#include "doctest.h"

TEST_CASE("test 1") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("3");
  map.push_back("3 2 1");

  CHECK(s.getSolution(map) == std::string("YES"));
}

TEST_CASE("test 2") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("4");
  map.push_back("4 1 3 2");

  CHECK(s.getSolution(map) == std::string("YES"));
}

TEST_CASE("test 3") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("3");
  map.push_back("2 3 1");

  CHECK(s.getSolution(map) == std::string("YES"));
}
