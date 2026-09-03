#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "solution.cpp"

#include <string>
#include <vector>

#include "doctest.h"

TEST_CASE("test 1") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("()[]");

  CHECK(s.getSolution(map) == std::string("yes"));
}

TEST_CASE("test 2") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("([)]");

  CHECK(s.getSolution(map) == std::string("no"));
}

TEST_CASE("test 3") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("(");

  CHECK(s.getSolution(map) == std::string("no"));
}
