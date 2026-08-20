#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>

std::vector<std::string> split_row(const std::string &str)
{
    std::vector<std::string> result;

    std::stringstream ss(str);
    std::string word;

    while (ss >> word)
    {
        result.push_back(word);
    }

    return result;
}

std::vector<char> split_row_to_chars(const std::string &str)
{
    std::vector<char> result;

    for (char c : str)
    {
        result.push_back(c);
    }

    return result;
}

std::vector<std::vector<char>> readRows()
{
    std::fstream fs("test_1.txt");
    std::vector<std::vector<char>> result;

    std::string row;

    while (std::getline(fs, row))
    {
        result.push_back(split_row_to_chars(row));
    }

    fs.close();

    return result;
}

void print(std::vector<std::vector<std::string>> rows)
{
    for (std::vector<std::string> row : rows)
    {

        for (std::string s : row)
        {
            std::cout << s << " ";
        }
        std::cout << std::endl;
    }
}

void print(std::vector<std::vector<char>> rows)
{
    for (std::vector<char> row : rows)
    {

        for (char s : row)
        {
            std::cout << s << " ";
        }
        std::cout << std::endl;
    }
}

int count_positions(std::vector<std::vector<char>> matrix)
{
    int rows = std::atoi(&matrix[0][0]);
    int cols = std::atoi(&matrix[0][2]);

    std::cout << "rows :" << rows << "cols :" << cols << std::endl;

    for (int row = 1; row <= rows; row++)
    {
        //
    }

    return 0;
}

int main()
{
    std::vector<std::vector<char>> rows = readRows();
    print(rows);
    count_positions(rows);

    return 0;
}
