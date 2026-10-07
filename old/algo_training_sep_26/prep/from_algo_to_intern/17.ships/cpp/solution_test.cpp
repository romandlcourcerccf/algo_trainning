#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "solution.h"

#include <string>
#include <vector>

#include "doctest.h"

TEST_CASE("test 1") {
  std::cout << ">>> 1 >>>" << std::endl;
  Solution s;

  std::vector<std::string> map;

  map.push_back("#.#.#.....");
  map.push_back(".......##.");
  map.push_back(".#..#.....");
  map.push_back(".#........");
  map.push_back(".#..##....");
  map.push_back("..........");
  map.push_back("####...#..");
  map.push_back(".......#..");
  map.push_back(".......#..");
  map.push_back("##........");

  CHECK(s.getSolution(map) == std::string("YES"));
}

TEST_CASE("test 2") {
  std::cout << ">>> 2 >>>" << std::endl;
  Solution s;

  std::vector<std::string> map;

  map.push_back("##..#.....");
  map.push_back(".......##.");
  map.push_back(".#..#....#");
  map.push_back(".#........");
  map.push_back(".#........");
  map.push_back("..........");
  map.push_back("####...#..");
  map.push_back(".......#..");
  map.push_back(".......#..");
  map.push_back("##.......#");

  CHECK(s.getSolution(map) == std::string("YES"));
}