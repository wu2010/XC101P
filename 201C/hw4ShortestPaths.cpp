#include <cmath>
#include <iostream>
#include <limits.h>
#include <vector>

using namespace std;

int shortest = INT_MAX;
int numOfPaths = 0;

void shortestpath(int x, int y, int pathLength, int a, int b,
      vector<vector<int>> &matrix, vector<vector<bool>> &visited) {

  if (x < 0 || x >= matrix.size() || y < 0 || y >= matrix.size()
    || matrix[x][y] == 1 || visited[x][y]) {
    return;
  }

  // reach the endpoint (a, b)
  /* While keeping track of the length of the shortest path so far,
  also keep track of the number of shortest paths - If you reach the goal position,
  and the path length is equal to the shortest path length, increment the number of
  shortest paths. If a path is found that is shorter, reset this variable back to 1. */
  if (x == a && y == b) {
    if (pathLength < shortest) {
      shortest = pathLength;
      numOfPaths = 1;
    } else if (pathLength == shortest) {
      numOfPaths++;
    }
  }

  visited[x][y] = true;

  shortestpath(x + 1, y, pathLength+1, a, b, matrix, visited);
  shortestpath(x - 1, y, pathLength+1, a, b, matrix, visited);
  shortestpath(x, y + 1, pathLength+1, a, b, matrix, visited);
  shortestpath(x, y - 1, pathLength+1, a, b, matrix, visited);

  visited[x][y] = false; // backtrack
};

int main() {
  int n;
  cin >> n;

  vector<vector<int>> matrix;
  vector<vector<bool>> visited;

  for (int i = 0; i < n; i++) {
    vector<int> temp;
    int k;
    for (int j = 0; j < n; j++) {
      cin >> k;
      temp.push_back(k);
    }
    matrix.push_back(temp);
    visited.push_back(vector<bool>(n, false));
  }

  // length include itself
  shortestpath(0, 0, 1, n - 1, n - 1, matrix, visited);

  cout << numOfPaths << endl;
  cout << shortest << endl;
}

/*
Description:
A mouse is trying to find its way through a labyrinth. The labyrinth is a square grid with size
n×n. The mouse starts at the upper left corner and needs to reach the lower right corner.
The mouse can only move down, up, left, or right to adjacent cells. It cannot visit a cell
more than once. Your task is to find the number of shortest paths and the length of
the shortest path/paths.

Input:
The first line contains a positive integer n (𝑛<50), which represents the size of the labyrinth.
The next n lines each have n numbers, either 0 or 1. A 0 means the cell can be passed through,
while a 1 means the cell cannot be passed through.

5
0 0 0 0 0
0 1 1 1 0
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0

Output:
The output consists of two lines:
The number of shortest paths from the upper left corner to the lower right corner.
The length of the shortest path from the upper left corner to the lower right corner.

1
9
*/
