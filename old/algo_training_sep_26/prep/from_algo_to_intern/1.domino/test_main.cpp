
#include <gtest/gtest.h>
#include "main.cpp"

// 1. The function we want to test
int Add(int a, int b)
{
    return a + b;
}

bool IsEven(int number)
{
    return number % 2 == 0;
}

// 2. The Unit Tests
// TEST(TestSuiteName, TestName)
TEST(AdditionTest, HandlesPositiveInputs)
{
    EXPECT_EQ(Add(1, 2), 3);
    EXPECT_EQ(Add(10, 20), 30);
}

TEST(AdditionTest, HandlesNegativeInputs)
{
    EXPECT_EQ(Add(-1, -1), -2);
    EXPECT_EQ(Add(-5, 5), 0);
}

TEST(IsEvenTest, HandlesEvenAndOdd)
{
    EXPECT_TRUE(IsEven(4));
    EXPECT_FALSE(IsEven(7));
}

// 3. The main function that triggers all tests
int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}