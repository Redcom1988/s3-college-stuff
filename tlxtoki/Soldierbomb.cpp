#include <bits/stdc++.h>
using namespace std;
#define ll long long

// soldier count, health
int n, health;
// soldier bombs, bombs[0] deals 1 dmg, bombs[1] divides health by 1/2, bombs[2] divides health by 1/3
vector<int> bombs; 
vector<ll> memo;

ll mpriceRec(int health) {
    // if health 0 then 0 price
    if (health <= 0) return 0;
    
    // if already calculated, return the value
    if (memo[health] != -1) return memo[health];
    
    // Initialize result with the cost of using bomb[0] repeatedly
    ll result = (ll)health * bombs[0];
    
    // Option 1: Use bomb[0] (deal 1 damage)
    result = min(result, mpriceRec(health - 1) + bombs[0]);
    
    // Option 2: Use bomb[1] (divide health by 2)
    result = min(result, mpriceRec((health + 1) / 2) + bombs[1]);
    
    // Option 3: Use bomb[2] (divide health by 3)
    result = min(result, mpriceRec((health + 2) / 3) + bombs[2]);
    
    // Memoize the result and return
    return memo[health] = result;
}

ll mprice(int n, vector<int>& bombs) {
    memo.assign(n + 1, -1); // Initialize memoization array with -1
    return mpriceRec(n);
}

int main() {
    bombs.resize(3);
    bombs[0] = 1;
    cin >> n >> bombs[1] >> bombs[2];
    
    for (int i = 0; i < n; i++) {
        cin >> health;
        cout << mprice(n, bombs) << endl;
    }

    return 0;
}