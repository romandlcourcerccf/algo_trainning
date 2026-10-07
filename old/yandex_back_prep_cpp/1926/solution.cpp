#include <queue>
#include <vector>

using namespace std;

class Solution {
 public:
  int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
    queue<vector<int>> q;

    maze[entrance[0]][entrance[1]] = '.';
    q.push(entrance);

    int radius = 0;

    while

      return 0;
  }
};

// void BFS(int start, vector<vector<int>>& graph, int vertices){
//     vector<bool> visited(vertices, false); // Track visited vertices
//     queue<int> q;
//     visited[start] = true; //Mark starting vertex as visited
//     q.push(start); // added to queue

//     while(!q.empty()){
//         int current = q.front(); // Get the next vertex to explore
//         q.pop(); // Remove it from queue
//         cout << current << " ";
//         // Visit all the neighbours of the current vertex
//         for(int neighbour : graph[current]){
//             if(!visited[neighbour]){ // if not visited
//                 visited[neighbour] = true; // mark as visited
//                 q.push(neighbour); // Add to the queue
//             }
//         }
//     }
// }