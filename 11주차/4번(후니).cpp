#include <iostream>
#define ll long long
#define MAX 1500001
using namespace std;
ll ans, n, t[MAX], p[MAX], dp[MAX];
int main() {
    cin>>n;
    for(int i=1; i<=n; ++i) {
        cin>>t[i]>>p[i];
    }
    
    for(int i=1; i<=n; ++i) {
        dp[i+1] = max(dp[i], dp[i+1]);
        dp[i+t[i]] = max(dp[i+t[i]], dp[i] + p[i]);
        // cout << i << " : " << dp[i+1] 
            << ",\t" <<  dp[i+t[i]] << ", " << t[i] << '\n';
    }
    
    cout<<dp[n+1];
    return 0;
}
