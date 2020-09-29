// to compile: g++ -std=c++17 <file_name>
typedef long long ll;
// to run: ./a.out
//
// fast compile: g++ -std=c++17 -Wshadow -Wall -o "%e" "%f" -O2 -Wno-unused-result
// more err compile: g++ -std=c++17 -Wshadow -Wall -o "%e" "%f" -g -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG
//
// declare dp array statically outside of main and then use memset or for loop to initialize
//
//
// debugging:
// - check for integer overflow (function return type, variables being used to sum)
// - inconsistent bugs/print statements -> accessing bad memory and just getting unlucky with no segfault


/********   All Required Header Files ********/
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

#define MOD 1000000007
#define INF 1e9
#define sum(a) accumulate(begin(a), end(a), 0, [](int a, int b) {return a+b;})

using namespace std;
typedef long long ll;

// const ll MOD = 998244353;

// COMMON MISTAKES:
// - integer overflow
// - integer overflow before modding
// - subtraction during modding
// - modding negative numbers, always make positive!

/*** Number Theory ***/
// CAREFUL: (-1) % X = -1 ACTUALLY BE FKING CAREFUL, SUBTRACTION TOO
// x, exp -> x^e mod MOD
ll mod_exp(ll x, ll exp) {
    ll res = 1;
    ll base = x % MOD;
    while (exp) {
        if (exp % 2 == 1) {
            res = (res * base) % MOD;
        }
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

ll mod_inv_prime(ll x) {
    return mod_exp(x, MOD-2);
}

ll gcd(ll a, ll b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

ll lcm(ll a, ll b) {
    return a*b/gcd(a,b);
}

// when result is x*y^-1 % MOD, just treat fractions as x*y^-1

/*** Graph ***/
unordered_map<int, int> bfs_dist(int v, unordered_map<int, vector<int>> &edges) {
    unordered_map<int, int> distances;
    unordered_set<int> seen;
    deque<tuple<int, int>> q;
    q.push_back(make_tuple(v,0));
    while (!q.empty()) {
        int curr, dist;
        tie(curr, dist) = q.front(); q.pop_front();
        if (seen.find(curr) != seen.end()) continue;
        seen.insert(curr);
        distances[curr] = dist;
        for (int ne : edges[curr]) {
            q.push_back(make_tuple(ne, dist+1));
        }
    }
    return distances;
}

// pass by value (object is copied, which is rarely wut we want)
void pass_by_value(vector<int> nums) {
  // for loop
  for (int i = 0; i < nums.size(); i++)
    cout << nums[i] << "\n";
}

// pass by reference (what we are used to)
void pass_by_reference(vector<int> &nums) {
// const vector<int> &nums if dont want to edit
  // for each loop
  for (int num: nums)
    cout << num << endl;
}

// pass by pointer (same effect as pass by reference but more annoying)
// need to pass in memory address to func call -- func(&nums)
// and dereference everytime we access things with -> and *
void pass_by_pointer(vector<int> * nums) {
  for (int num: *nums)
    cout << num << endl;
}

auto test2() {
  return vector<int>(10, 5);
}

int globalarray[100]; // init global array
int main() {
  int myarray[] = {1, 2, 3}; // init array to list
  memset(myarray, 0, sizeof(myarray)); // init array to all 0

  vector<int> res; // init vector to empty
  vector<int> arr = {1, 2, 3}; // init vector to list
  vector<int> filled(3, 0); // init vector to 3 0's
  vector<int> slice(begin(myarray)+1, end(myarray)); // slicing vector
  vector<vector<int>> matrix = {{1,2,3},{1,2,3},{1,2,3}}; // init 2d vector to matrix
  vector<vector<int>> matrix2(100, vector<int>(100, 0)); // init 2d vector to all 0
  res.push_back(1); res.back(); res.pop_back(); // push, peek, pop last element
  int maxel = *max_element(begin(arr), end(arr));
  cout << maxel << endl;
  sort(begin(arr), end(arr), [](int a, int b) {return a > b;});
  cout << arr[0] << arr[1] << arr[2] << endl;

  deque<int> q;
  q.push_back(1); q.back(); q.pop_back(); q.push_front(1); q.front(); q.pop_front(); 

  string hello = "Hello world!"; // init string to string literal
  string hellon = "test" + hello + "\n"; // concatenate string with string literal, can't concatenate literal with literal!
  char c = hello[1];
  cout << c << endl;
  int a = 5, b = 5;
  cout << hello << a << b << hellon;

  // for unordered_map, map, unordered_set, set:
  // insertion: hm[k] = v,  set.insert(k)
  // find: hm.find(k) != hm.end(), set.find(k) != set.end() (or use hm.count(k) > 0, set.count(k) > 0)
  // access: hm[k] (if hm[k] does not exist, then hm[k] is created and set to default value)
  // removal: hm.erase(k), set.erase(k)
  // insertion only if k not in hm: hm.insert()
  unordered_map<int, int> hm; // init unordered map (hm) to empty
  hm[4] = 20; // insert kv pair into hm
  bool contains = hm.find(4) != hm.end(); // check if key in hm
  int val = hm[4]; // access value with key
  cout << contains << val << endl;

  map<int, int> bst; // init ordered map (bst) to empty

  unordered_set<int> keys; // init unordered map (set of keys) to empty

  set<int> bstkeys; // init ordered set (bst of keys) to empty

  tuple<int, int> tup {0, 1}; // or make_tuple(0, 1);
  // tuple<int, int> t = {1, 5}; // in C++17
  // auto [a, b, c] = tup // in C++17
  int first = 1, second = 2;
  first = get<0>(tup); // access element of tuple
  get<1>(tup) = second; // modify element of tuple
  tie(first, second) = tup; // unpack tuple, can use ignore to ignore stuff
  cout << first << second << endl;

  int x = 0, y = 1;
  swap(x, y); // swap util

  // priority queue - max heap
  priority_queue<pair<int,int>> pq;
  priority_queue<tuple<int,int,int>> pqt;
  pq.push({2, 3});
  pq.push({4, 6});
  cout << pq.top().second << endl; pq.pop();
  cout << pq.top().second << endl; pq.pop();
  pqt.push(make_tuple(1,2,2));
  pqt.push(make_tuple(5,0,0));
  pqt.push(make_tuple(2,1,1));
  cout << get<1>(pqt.top()) << endl; pqt.pop();
  cout << get<1>(pqt.top()) << endl; pqt.pop();
  cout << get<1>(pqt.top()) << endl; pqt.pop();
  
  // stdout stuff
  // reading array input
  vector<vector<int>> lists(2, vector<int>(2));
  for (vector<int>& l : lists) {
      for (int& x : l) {
          x = 5; // cin >> x;
      }
  }

  cout << "--------" << endl;

}
