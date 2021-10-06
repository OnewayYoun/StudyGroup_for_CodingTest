#include <string>
#include <vector>
#include <iostream>
using namespace std;

int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};
vector<vector<int>> board;
int rotate(vector<int> q) {
    int x1 = q[0]-1, y1 = q[1]-1, x2 = q[2]-1, y2 = q[3]-1;
    int len, xlen = x2 - x1, ylen = y2 - y1;
    int x = x1, y = y1;
    int min_num = 1e9;
    
    int tmp, tmp2=board[x][y];
    for(int w=0; w<4; ++w) {
        if(w%2==0)  len = ylen;
        else        len = xlen;
        
        for(int l=0; l<len; ++l){
            int nx = x+dx[w], ny = y+dy[w];
            // cout << x << ", " << y << " : " << board[x][y] <<
                // " >> " << x + dx[w] << ", " << y + dy[w] << " : " << board[x + dx[w]][y + dy[w]] << '\n';
                
            tmp = tmp2;
            tmp2 = board[nx][ny];
            board[nx][ny]= tmp;
            
            x = nx, y = ny;
            min_num = min(min_num, board[nx][ny]);
        }
    }
    
    return min_num;
}

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    
    vector<int> b(columns);
    vector<vector<int>> bb(rows, b);
    
    for(int x=0; x<rows; ++x) {
        for(int y=0; y<columns; ++y) {
            bb[x][y] = rows*x + y + 1;
        }
    }
    board = bb;
    
    for(vector<int> query : queries) {
        int min_num = rotate(query);
        
        // for(int x=0; x<rows; ++x) {
        //     for(int y=0; y<columns; ++y) {
        //         cout<<board[x][y]<<' ';
        //     } cout<<'\n';
        // } cout<<'\n';
        answer.push_back(min_num);
    }
    
    return answer;
}
