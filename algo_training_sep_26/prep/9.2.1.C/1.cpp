#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <sstream>
#include <algorithm>
#include <iterator>

std::vector<int> parse_to_vec(std::string &s)
{
    std::istringstream iss(s);

    std::vector<int> vec((std::istream_iterator<int>(iss)),
                         std::istream_iterator<int>());

    return vec;
}

void write_to_file(std::set<int> _set)
{
    std::ofstream out_file("output.txt");

    for (int val : _set)
    {
        out_file << val << " ";
    }

    out_file << std::endl;
    out_file.close();
}

void write_to_file(std::vector<int> _set)
{
    std::ofstream out_file("output.txt");

    for (int val : _set)
    {
        out_file << val << " ";
    }

    out_file << std::endl;
    out_file.close();
}

int main()
{
    std::fstream file("input.txt");

    std::string row1;
    std::string row2;

    if (!file.is_open())
    {
        std::cerr << "Could not open" << std::endl;
        return 1;
    }

    std::getline(file, row1);
    std::getline(file, row2);

    std::vector<int> vec1 = parse_to_vec(row1);
    std::vector<int> vec2 = parse_to_vec(row2);

    std::set<int> s1(vec1.begin(), vec1.end());
    std::set<int> s2(vec1.begin(), vec1.end());
    std::set<int> intersection_set;

    std::set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), std::inserter(intersection_set, intersection_set.begin()));

    std::vector<int> res(intersection_set.begin(), intersection_set.end());

    std::sort(res.begin(), res.end());

    write_to_file(res);

    file.close();

    return 0;
}