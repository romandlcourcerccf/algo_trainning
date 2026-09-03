#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "solution.cpp"

#include <string>
#include <vector>

#include "doctest.h"

TEST_CASE("test 1") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("1");

  CHECK(s.getSolution(map) == std::string("1"));
}

TEST_CASE("test 2") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("2");

  CHECK(s.getSolution(map) == std::string("2"));
}

TEST_CASE("test 4") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("4");

  CHECK(s.getSolution(map) == std::string("7"));
}

TEST_CASE("test 5") {
  Solution s;

  std::vector<std::string> map;

  map.push_back("5");

  CHECK(s.getSolution(map) == std::string("13"));
}