#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>


std::vector<std::string> read_file(const std::string& input){
     std::ifstream input_file("1.txt");

    if(!input_file.is_open()) {
        std::cerr << "Could not open!" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(input_file, line));
    return line;
    
}
std::vector<int> to_int_array(const std::string& input){

    std::vector<int> res;
    std::stringstream ss(input);
    std::string word;
    
    while (ss >> word) {
        res.push_back(std::stoi(word));
    }

    return res;

}

int main(){

    std::ifstream input_file("1.txt");

    if(!input_file.is_open()) {
        std::cerr << "Could not open!" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(input_file, line));
    std::vector<int> int_wec = to_int_array(line);
    std::sort(int_wec.begin(), int_wec.end());

 
    if (int_wec.at(0) * int_wec.at(1) > int_wec.at(int_wec.size()-1) * int_wec.at(int_wec.size()-2)) {
        std::cout << int_wec.at(0) <<" "<<int_wec.at(1)<<std::endl;
    } else {
        std::cout << int_wec.at(int_wec.size()-1) <<" "<<int_wec.at(int_wec.size()-2)<<std::endl;
    }

    input_file.close();

    
    return 0;
}