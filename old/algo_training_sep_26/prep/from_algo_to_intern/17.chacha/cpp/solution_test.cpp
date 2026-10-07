#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "solution.h"

#include "doctest.h"

TEST_CASE("test 1") {
  std::cout << ">>> 1 >>>" << std::endl;
  Solution s;
  CHECK(s.getSolution("ABACABA") == std::string("B"));
}

TEST_CASE("test 2") {
  std::cout << ">>> 2 >>>" << std::endl;
  Solution s;
  CHECK(s.getSolution("AZAA") == std::string("Y"));
}

TEST_CASE("test 3") {
  std::cout << ">>> 3 >>>" << std::endl;
  Solution s;
  CHECK(s.getSolution("ABABAB") == std::string("A"));
}