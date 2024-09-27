class Solution:
    
    def maxStep(self, arr):
        #Your code here
        max_steps=0
        cur_steps=0
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                cur_steps+=1
                if(cur_steps>max_steps):
                    max_steps=cur_steps
            else:
                cur_steps=0
        return max_steps

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()


 void mirror(Node* node) {
        if(node == NULL){
            return;
        }
        mirror(node->left);
        mirror(node->right);
        Node* temp = node->left;
        node->left = node->right; 
        node->right = temp;
    }
 
 class Solution {
public:
    void DFS(int node, vector<bool>& visited, vector<vector<int>>& adj) {
        visited[node] = true;
        
        for (auto v : adj[node]) {
            if (!visited[v])
                DFS(v, visited, adj);
        }
    }

    int isCircle(vector<string>& arr) {
        vector<int> inDeg(26, 0);
        vector<int> outDeg(26, 0);
        vector<vector<int>> adj(26);

        //Step 1 Create adjacency list
       //Step 2: Calculate indegree and outdegree of nodes simultaneously.


        for (auto A : arr) {
            int u = A[0] - 'a';
            int v = A[A.size() - 1] - 'a';
            
            adj[u].push_back(v);
            inDeg[v]++;
            outDeg[u]++;
        }
        //For eucleian Circuit to exist, indegree and outdegree of a node should be same.
        for (int i = 0; i < 26; i++) {
            if (inDeg[i] != outDeg[i])
                return false;
        }
        
       // Graph Traversal
        vector<bool> visited(26, false);
        int node = arr[0][0] - 'a';
        DFS(node, visited, adj);
        // check all nodes are visited or not.
        for (int i = 0; i < 26; i++) {
            if (inDeg[i] && !visited[i])
                return false;
        }
        
        return true;
    }
};
 
 
 
 
 
 
 
 class Solution {
    public:
    int minimumCostPath(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> dist(n, vector<int>(n, 1e9));
        dist[0][0] = grid[0][0];
        
        int drow[] = {-1, 0, 1, 0};
        int dcol[] = {0, 1, 0, -1};
        
        priority_queue<pair<int,pair<int,int>>, vector<pair<int,pair<int,int>>>, greater<pair<int,pair<int,int>>>> pq;
        pq.push({grid[0][0], {0, 0}});
        
        while(!pq.empty()){
            auto it = pq.top();
            pq.pop();
           
            int cost = it.first;,
            int row = it.second.first;
            int col = it.second.second;
           
            if(row == n-1 && col == n-1) return cost;
           
            for(int i=0; i<4; i++) {
                int nrow = row + drow[i];
                int ncol = col + dcol[i];
                
                if(ncol >= 0 && ncol < n && nrow >= 0 && nrow < n && dist[nrow][ncol] > cost + grid[nrow][ncol]) {
                    dist[nrow][ncol] = cost + grid[nrow][ncol];
                    pq.push({dist[nrow][ncol], {nrow, ncol}});
                }
            }
        }
        return 0;
    }
};