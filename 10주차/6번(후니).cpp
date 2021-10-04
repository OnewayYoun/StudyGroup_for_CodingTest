#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>
#include <cmath>
using namespace std;
int n,c,m,t1,t2,box, load, ans;
struct Truck { int t1,t2,box; };
vector<Truck> info;

int main() {
    cin>>n>>c>>m;
    for(int i=0;i<m;++i){
        cin>>t1>>t2>>box;
        info.push_back({t1, t2, box});
    }
    vector<int> truck(n);
    sort(info.begin(), info.end(), [](const auto a, const auto b){
        return a.t2 < b.t2;
    });
        
    for(int i=0;i<m;++i){
        auto [t1,t2,box] = info[i];
        --t1, --t2;
        // cout << i << " : " << t1 << ", " << t2 << ", " << box << '\n';
        
        int tmp = 0;
        for(int j=t1; j<t2; ++j) {
            tmp = max(tmp, truck[j]);
        }
        // cout << "\t" << tmp << '\n';
        
        int cnt = 0;
        if(tmp+box <= c) cnt = box;
        else cnt = c - tmp;
        
        for(int j=t1; j<t2; ++j) {
            truck[j] += cnt;
        }
        ans += cnt;
        
        // cout<<"\t";
        // for(int j=0; j<n; ++j) cout << truck[j] << ", "; cout<<'\n';
    }
    
    cout << ans;
    return 0;
}
