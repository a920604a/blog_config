---
title: 212. Word Search II
tags:  
    - backtracking
    - trie
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/word-search-ii/)

## solution

- option 1 - backtracking
time out
```c++
class Solution {
public:
    bool traverse(vector<vector<char>>& board, vector<vector<bool>>& visited, int i, int j, string &word, int cur){
        int n = board.size(), m = board[0].size();
        if(cur==word.size()) return true;
        if(i<0 || j<0 || i>n-1 || j>m-1 || visited[i][j] || word[cur]!=board[i][j]) return false;
        
        visited[i][j] = true;
        bool ret = traverse(board, visited, i-1, j, word, cur+1) || \
            traverse(board, visited, i+1, j, word, cur+1) || \
            traverse(board, visited, i, j-1, word, cur+1) || \
            traverse(board, visited, i, j+1, word, cur+1);
        visited[i][j] = false;
        return ret;
        
    }
    
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        set<string> ret;
        int n = board.size(), m = board[0].size();
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        
        for(string word:words){
            for(int i=0;i<n;++i){
                for(int j=0;j<m;++j){
                    if(traverse(board, visited, i, j, word, 0)) ret.insert(word);
                }
            }
            
        }
        return vector<string> (ret.begin(), ret.end());
    }
};
```

##### option - Trie
必須要用Trie 資料結構，為words建立



## analysis
