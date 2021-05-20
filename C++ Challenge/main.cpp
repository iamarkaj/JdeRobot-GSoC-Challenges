#include<bits/stdc++.h>
using namespace std;


const int row=5,col=7;
int k=0,depth_count=0;
bool visited[row][col];
vector<string>  grid;
vector<int> db[2];


void dfs(int x, int y) {
    if (x < 0 || y < 0 || x > row || y > col || visited[x][y] || grid[x][y] == '#')
        return;
    visited[x][y] = true;
    db[k].push_back(x);
    db[k].push_back(y);
    k++;
    depth_count++;
    dfs(x,y+1); // go down
    dfs(x,y-1); // go up
    dfs(x+1,y); // go right
    dfs(x-1,y); // go left
}



int main(){


    int i,j;


    // read from schema
    fstream schemaread;
    schemaread.open("schema.txt",ios::in);
    if (schemaread.is_open()){
       string x;
       while(getline(schemaread, x)){
          grid.push_back(x);
       }
       schemaread.close();
    }



    // find holes in first row
    bool openings[col];
    int num_of_openings=0;
    for(i=0;i<col;i++) {
        if(grid[0][i]=='.') {
            openings[i]=true;
            num_of_openings++;
        }
        else {
            openings[i]=false;
        }
    }



    // return if there is no opening
    if(num_of_openings==0) {
        cout<<"No Holes present in the first row"<<endl;
        return 0;
    }



    // store depth count of all openings
    int depth_of_openings[num_of_openings];
    j=0;
    for(i=0; i<col;i++) {
        if (openings[i]) {
            dfs(0,i);
            depth_of_openings[j]=depth_count;
            j++;
            depth_count=0;
        }
    }



    // find the max depth count
    int _max=depth_of_openings[0];
    int idx_of_max=0;
    for(i=1;i<num_of_openings; i++) {
        if(depth_of_openings[i]>_max) {
            _max=depth_of_openings[i];
            idx_of_max=i;
        }
    }



    // store the positions of longest path
    int store_path[_max][2];
    j=0;
    int starting_pos=0;
    for(i=0;i<idx_of_max;i++) {
        starting_pos+=depth_of_openings[i];
    }
    for(i=starting_pos; i<starting_pos+_max;i++) {
        store_path[j][0]=db[i][0];
        store_path[j][1]=db[i][1];
        j++;
    }



    // initialize required matrix
    string required_matrix[row][col];
    for(i=0; i<row;i++) {
        for(j=0;j<col;j++) {
            required_matrix[i][j]="#";
        }
    }



    // replace certain positions of required matrix with numbers
    for(int i=0;i<_max;i++) {
        required_matrix[store_path[i][0]][store_path[i][1]]=to_string(i);
    }



    // write to file
    ofstream schemawrite("output.txt");
    schemawrite<<_max<<"\n";
    for(int i=0;i<row;i++) {
        for(j=0;j<col;j++) {
            schemawrite<<required_matrix[i][j];
        }
        schemawrite<<"\n";
    }
    schemawrite.close();
}
