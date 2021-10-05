#include <vector>
#include <iostream>
#define F(i,n) for(int i=0;i<n;++i)
using namespace std;
// 가로, 세로, 우측하단대각선, 우측상단대각선
int dx[]={0,1,1,-1};
int dy[]={1,0,1,1};
int n, board[19][19];

bool chk(int x, int y) {
    return !(x<0||y<0||x>=n||y>=n);
}

int main() {
    n = 19;
    F(x, n) F(y, n) cin>>board[x][y];
    
    F(x, n) F(y, n) {
        if(!board[x][y]) continue;
        // cout<<"CHECK : " << x << ", " << y << '\n';

        F(w, 4) {
            bool fail = false;
            if(chk(x-dx[w], y-dy[w]) && board[x][y] == board[x-dx[w]][y-dy[w]]) continue;
            
            F(a, 6) {
                int nx=x + dx[w]*a, ny=y + dy[w]*a;
                // cout<<"\t : " << w << " : " << nx << ", " << ny << '\n';

                if(a<5 && (!chk(nx, ny) || board[x][y] != board[nx][ny])) {
                    fail = true;
                    break;
                }

                if(a==5 && board[x][y] == board[nx][ny]) {
                    fail = true;
                    break;
                }
            }

            if(!fail) {
                cout << board[x][y] << '\n';
                cout<< x+1 << ' ' << y+1 << '\n';
                return 0;
            }
        }
    }
    
    cout<< 0 << '\n';
    return 0;
}
