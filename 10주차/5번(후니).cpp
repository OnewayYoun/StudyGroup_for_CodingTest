#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int n,map[21][21], ans=1e9;
int main()
{
    cin>>n;
    for(int x=0;x<n;++x) {
        for(int y=0;y<n;++y) {
            cin>>map[x][y];
        }
    }
    
    vector<int> v(n);
    for(int i=0;i<n/2;++i) v[n-1-i] = 1;

    
    do{
        // for(int i : v) cout<<i<<", "; cout<< '\n';
        int sum_s = 0, sum_l = 0;
        
        vector<int> s, l;
        for(int i=0; i<v.size(); ++i) {
            if(v[i] == 1) s.push_back(i);
            else l.push_back(i);
        }
        
        for(int x=0;x<s.size()-1;++x){
            for(int y=x+1;y<s.size();++y){
                sum_s += map[s[x]][s[y]] + map[s[y]][s[x]];
            }
        }
        for(int x=0;x<l.size()-1;++x){
            for(int y=x+1;y<l.size();++y){
                sum_l += map[l[x]][l[y]] + map[l[y]][l[x]];
            }
        }
        
        ans = min(ans, abs(sum_s - sum_l));
        // cout<< "\t" << ans << '\n';
        
    } while(next_permutation(v.begin(), v.end()));
    
    cout << ans;
    return 0;
}
