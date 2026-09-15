#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "solution.cpp"

#include <string>
#include <vector>

#include "doctest.h"

TEST_CASE("test 1") {
  Solution s;
  std::vector<std::string> map;
  map.push_back("8 9 + 1 7 - *");
  CHECK(s.getSolution(map) == std::string("-102"));
}
