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


// Let A be 1-indexed arr, BIT[1...N]
// each index BIT[i] stores the sum A[i-lsb(i)+1] + ... + A[i]
// e.g. BIT[1] = A[1], BIT[2] = A[1] + A[2], BIT[4] = A[1] + A[2] + A[3] + A[4]
// BIT[6] = A[5] + A[6], BIT[12] = A[9] + A[10] + A[11] + A[12]
// Generalizes to all operations that are associative and have an inverse

const int N = 100;
int BIT[N];

void update(int i, int val) {
    i++; // convert 0-index to 1-index, since we are updating fenceposts
    while (i <= N) {
        BIT[i-1] += val;
        i += (i & -i);
    }
}

// 0-indexed operations
// returns A[0] + ... A[i-1]
int query(int i) {
    int csum = 0;
    while (i > 0) {
        csum += BIT[i-1];
        i -= (i & -i);
    }
    return csum;
}

// returns A[i] + ... A[j-1]
int rangequery(int i, int j) {
    return query(j) - query(i);
}

// test range sum queries
int main() {
    int arr[N];
    map<pair<int,int>, int> csums;
    for (int i = 0; i < N; i++) {
        arr[i] = i+1;
    }
    for (int i = 0; i < N; i++) {
        int csum = 0;
        csums[make_pair(i, i)] = 0;
        for (int j = i; j < N; j++) {
            csum += arr[j];
            csums[make_pair(i, j+1)] = csum;
        }
    }

    for (int i = 0; i < N; i++) {
        update(i, arr[i]);
    }

    for (int i = 0; i < N; i++) {
        for (int j = i; j < N+1; j++) {
            if (rangequery(i, j) != csums[make_pair(i,j)]) { cout << "ERR" << endl;}
        }
    }
}
