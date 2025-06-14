#include <cmath>
#include <iostream>
#include <limits.h>
#include <vector>
#include <deque>

using namespace std;

int largest = 0;

int reachConnected(deque<pair<int, int>> toVisit, int pathLength,
      int n, int m,
      vector<vector<int>> &matrix, vector<vector<bool>> &visited) {

  // breadth first search
  while (toVisit.size() > 0) {

    pair<int, int> p = toVisit.front();
    toVisit.pop_front();

    if (visited[p.first][p.second]) {
      continue;
    }

    // only handle not visited cell
    visited[p.first][p.second] = true;
    pathLength++;

    if (p.first - 1 >= 0 && matrix[p.first - 1][p.second] == 1 && !visited[p.first - 1][p.second]) {
      toVisit.push_back(make_pair(p.first - 1, p.second));
    }
    if (p.first + 1 < n && matrix[p.first + 1][p.second] == 1 && !visited[p.first + 1][p.second]) {
      toVisit.push_back(make_pair(p.first + 1, p.second));
    }
    if (p.second - 1 >= 0 && matrix[p.first][p.second - 1] == 1 && !visited[p.first ][p.second - 1]) {
      toVisit.push_back(make_pair(p.first, p.second - 1));
    }
    if (p.second + 1 < m && matrix[p.first][p.second + 1] == 1 && !visited[p.first][p.second + 1]) {
      toVisit.push_back(make_pair(p.first, p.second + 1));
    }

  }

  return pathLength;
}

int main() {
  int n, m;
  cin >> n;
  cin >> m;

  vector<vector<int>> matrix;
  vector<vector<bool>> visited;

  for (int i = 0; i < n; i++) {
    vector<int> temp;
    string s;
    cin >> s;
    const char * cs = s.c_str();
    for (int j = 0; j < m; j++) {
      temp.push_back(cs[j] == '0' ? 0 : 1);
    }
    matrix.push_back(temp);
    visited.push_back(vector<bool>(m, false));
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      deque<pair<int, int>> toVisit = deque<pair<int, int>>();
      // the same criteria will be used again and again
      if (matrix[i][j] == 1 && !visited[i][j]) {
        toVisit.push_back(make_pair(i, j));
      }
      int length = reachConnected(toVisit, 0, n, m, matrix, visited);
      if (length > largest) {
        largest = length;
      }
    }
  }

  cout << largest << endl;
}

/*
Description:
To navigate through the Sea of Trash, Martin creates a map with rows numbered from 1 to n
and columns numbered from 1 to m. Two cells that are vertically or horizontally adjacent are
considered connected. For example, (x, y) is connected to the cells (x-1, y), (x+1, y),
(x, y-1), and (x, y+1).

Each cell may or may not contain trash. Trash is represented on the map by a 1,
while trash-free cells are represented with a 0. A "trash block" is defined as a
connected region of adjacent trash cells. Given a map, find how many trash cells
are contained within the largest trash block.

You can refer to the examples for a better understanding of the problem.

Input:
The first line has two numbers, n and m.
The next n lines each contain m numbers, which are either 1 or zero.

5 4
0101
0111
1000
1100
0101


Output:
A single integer.

5
*/