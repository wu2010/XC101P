#include <cmath>
#include <iostream>
#include <limits.h>
#include <vector>
#include <deque>

using namespace std;

void attempt(int n, int p, vector<int> &assignment, int c,
    int &mincost, vector<vector<int>> &cost) {
  for (int i = 0; i < n; i++) {
    if (assignment[i] == -1) {
      assignment[i] = p;
      c += cost[i][assignment[i]];

      if (p == n-1) {
        // this is the last person assigned.
        if (c < mincost) {
          mincost = c;
        }
      } else {
        // if cumulated cost is less than mincost, then we can continue to assign
        if (c < mincost) {
          attempt(n, p + 1, assignment, c, mincost, cost);
        }
      }

      // restore the state for backtracking
      c -= cost[i][assignment[i]];
      assignment[i] = -1;
    }
  }
}

int assign(int n, vector<vector<int>> &cost) {

  vector<int> assignment(n, -1);

  // initialize the cost of the diagonal assignment
  int mincost = 0;
  for (int i = 0; i < n; i++) {
    mincost += cost[i][i];
  }

  // iterate over all assignments
  // find the minimum cost
  attempt(n, 0, assignment, 0, mincost, cost);
  return mincost;
}

int main() {
  int n;
  cin >> n;

  vector<vector<int>> cost(n);

  for (int i = 0; i < n; i++) {
    cost[i] = vector<int>(n);
    for (int j = 0; j < n; j++) {
      cin >> cost[i][j];
    }
  }

  cout << assign(n, cost);
}