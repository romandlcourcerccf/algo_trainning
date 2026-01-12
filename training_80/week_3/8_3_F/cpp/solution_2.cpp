#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

std::vector<std::string> split(const std::string& str) {
    std::vector<std::string> tokens;
    std::istringstream iss(str);

    std::string token;
    
    while (iss >> token) {
        tokens.push_back(token);
    }

    return tokens;
}

void print_tree(const std::map<int, std::vector<int>>& tree) {

      for (const auto &pair : tree) {
        
        std::cout<<pair.first<<":"<<"{";

        for (const auto v :  pair.second) {
            std::cout<< v << ",";
        }

        std::cout<<"}"<<std::endl;

    }
}

void dfs(int root, std::set<int> track, std::map<int,  std::set<int>>& tracks, std::map<int, std::vector<int>> &tree) {


    tracks[root] = track;

    track.insert(root);
    
    for (const auto &child: tree[root]) {
        dfs(child, track, tracks, tree);
    }
  

}

int main(){

    
    int nodes_number;
    string nodes;
    int pairs_number;

    string line;

    std::getline(std::cin, line);
    nodes_number = stoi(line);
    std::getline(std::cin, line);
    nodes = line;
    std::getline(std::cin, line);
    pairs_number = stoi(line);

    // std::cout <<  "nodes_number : " << nodes_number << std::endl;
    // std::cout <<  "nodes : " << nodes << std::endl;   
    // std::cout <<  "pairs_number : " << pairs_number << std::endl;  
    
    std::vector<std::string> nodes_list = split(nodes);

    std::map<int, std::vector<int>> tree;
    std::map<int,  std::set<int>> tracks;
    std::map<int, int> pairs;


    int root;
    for (int i=0; i < nodes_list.size(); i++) {

        int node = stoi(nodes_list[i]);

        if (node == 0) {
            root = i+1;
        }

        tree[node].push_back(i+1);
    }

    for (int i = 0; i < pairs_number; i++) {
        std::getline(std::cin, line);
        std::vector<std::string> pair = split(line);

        int p0 = stoi(pair[0]);
        int p1 = stoi(pair[1]);

        

    }

    std::set<int> track;
    dfs(root, track, tracks, tree);

    tree.clear();

    for (int i = 0; i < pairs_number; i ++) {
        std::getline(std::cin, line);
        std::vector<std::string> pair = split(line);

        int p0 = stoi(pair[0]);
        int p1 = stoi(pair[1]);
        
        if (tracks[p1].contains(p0)) {
            std::cout << '1' << std::endl;
        } else {
            std::cout << '0' << std::endl;
        }
    }
    

    return 0;
}