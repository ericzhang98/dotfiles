// implementation of Fenwick/Binary Index Tree

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;


const int N = 10000;
const int K = 25;
int st[N][K+1];
int logs[N+1];

void build(int arr[]) {
  logs[1] = 0;
  for (int i = 2; i <= N; i++)
      logs[i] = logs[i/2] + 1;
  for (int i = 0; i < N; i++) {
    st[i][0] = arr[i];
  }
  for (int j = 1; j <= K; j++)
    for (int i = 0; i + (1 << j) <= N; i++)
        st[i][j] = min(st[i][j-1], st[i + (1 << (j - 1))][j - 1]);
}

int rmquery(int L, int R) {
  int j = floor(log2(R - L + 1));
  int minimum = min(st[L][j], st[R - (1 << j) + 1][j]);
  return minimum;
}


// test range min queries
int main() {
    int arr[N];
    map<pair<int,int>, int> rmins;
    for (int i = 0; i < 10; i++) {
        arr[i] = i+1;
    }
    for (int i = 0; i < 10; i++) {
        for (int j = i; j < 10; j++) {
            int rmin = *min_element(arr+i, arr+j);
            rmins[make_pair(i, j)] = rmin;
        }
    }

    build(arr);

    for (int i = 0; i < 10; i++) {
        for (int j = i; j < 10; j++) {
            if (rmquery(i, j) != rmins[make_pair(i,j)]) { cout << "ERR" << endl;}
        }
    }
}
