#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "solution.h"

#include <vector>

#include "doctest.h"

TEST_CASE("testing factorial") {
  Solution s;

  vector<vector<char>> maze = {
      {'+', '+', '.', '+'}, {'.', '.', '.', '+'}, {'+', '+', '+', '.'}};
  vector<int> entrance = {1, 2};

  CHECK(s.nearestExit(maze, entrance) == 1);
}
