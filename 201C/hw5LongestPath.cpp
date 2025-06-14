#include <cmath>
#include <iostream>
#include <limits.h>
#include <vector>
#include <deque>

using namespace std;

int largest = 0;

bool isValidStart(int a, int b, int n , int m, vector<vector<int>>& matrix) {
  int value =  matrix[a][b];

  // use inverse statement on what cannot happen
  if ((a - 1 >= 0 && matrix[a - 1][b] > value) ||
    (a + 1 < n && matrix[a + 1][b] > value) ||
    (b - 1 >= 0 && matrix[a][b - 1] > value) ||
    (b + 1 < m && matrix[a][b + 1] > value)) {
    return false;
  }

  return true;
}

// return the largest length to start with (a, b)
int longestSki(int a, int b, int n , int m,
      vector<vector<int>> &matrix, vector<vector<bool>> &visited) {

  visited[a][b] = true;

  int value =  matrix[a][b];

  int maxLength = 0;

  if (a - 1 >= 0 && matrix[a - 1][b] < value && !visited[a - 1][b]) {

    maxLength = longestSki(a - 1, b, n, m, matrix, visited);
  }
  if (a + 1 < n && matrix[a + 1][b] < value && !visited[a + 1][b]) {

    int length = longestSki(a + 1, b, n, m, matrix, visited);
    if (length > maxLength) {
      maxLength = length;
    }
  }
  if (b - 1 >= 0 && matrix[a][b - 1] < value && !visited[a ][b - 1]) {

    int length = longestSki(a, b - 1, n, m, matrix, visited);
    if (length > maxLength) {
      maxLength = length;
    }
  }
  if (b + 1 < m && matrix[a][b + 1] < value && !visited[a][b + 1]) {

    int length = longestSki(a, b + 1, n, m, matrix, visited);
    if (length > maxLength) {
      maxLength = length;
    }
  }

  visited[a][b] = false;

  return 1 + maxLength;
}

int main() {
  int n, m;
  cin >> n;
  cin >> m;

  vector<vector<int>> matrix(n, vector<int>(m));
  vector<vector<bool>> visited(n, vector<bool>(m));

  for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
          cin >> matrix[i][j];
      }
  }

  for(int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      // determine a start point (i, j)
      if (isValidStart(i, j, n, m, matrix)) {
        int pathLength = longestSki(i, j, n, m, matrix, visited);
        if (pathLength > largest) {
          largest = pathLength;
        }
      }
    }
  }

  cout << largest << endl;
}

/*

This problem requires finding the longest ski path in a 2D ski area. The ski area is
represented by a 2D matrix, with each element indicating the height of the spot.
Michael wants to follow a path that has an incline only in the downward direction,
i.e. he can only switch to neighboring spots whose height is lower than his current spot.

For example, in the provided matrix, Michael can start from 24, ski down to 17,
then to 16, and finally end at 1, following the path 24-17-16-1. It is also possible
that Michael could follow the path 25-24-23-...-3-2-1 which is the longest path.
In this case, Michael starts at the spot with the highest height and will end at the spot
with the lowest height in the matrix. The ski area is represented by a 2D array,
and Michael can only move to its neighbors either to its left, right, up or down,
but not diagonally. The objective of this problem is to find the length of the
longest path that Michael can take, beginning at the highest point and ending
at the lowest point.

Input
1st line has two integers, the row number R and column number C.

Then there are R lines. Each line has C numbers. These numbers describe the
heights of those corresponding spots. Numbers are separated by a space.

5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

Output
One number as the length of the longest ski route/path within that given ski area.

25
*/