#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "solution.cpp"

#include <string>
#include <vector>

#include "doctest.h"

TEST_CASE("test 1") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("10");
  map.push_back("1 2 3 2 1 4 2 5 3 1");

  CHECK(s.getSolution(map) == std::string("-1 4 3 4 -1 6 9 8 9 -1"));
}
