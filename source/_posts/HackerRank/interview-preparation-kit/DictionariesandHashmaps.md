---
title: Dictionaries and Hashmaps
categories: 
    - HackerRank
comments: false
---

## Hash Tables: Ransom Note
字典的使用

### python solution
```python
def checkMagazine(magazine, note):
    # Write your code here
    mp = dict()
    for word in magazine:
        mp[word] = mp.get(word, 0)+1
    for word in note:
        if mp.get(word,0)==0:
            print("No")
            return
        else :
            mp[word]-=1
    print("Yes")
```
### c++ solution
```c++
void checkMagazine(vector<string> magazine, vector<string> note) {
    unordered_map<string, int> mp;
    for(string str:magazine) mp[str]++;
    for(string n:note){
        if(mp[n]==0){
            cout<<"No";
            return ;
        }
        else mp[n]--;
    }
    cout<<"Yes";
    return;

}
```

### analysis
- time complexity `O(n)`
- space complexity `O(n)`
## Two Strings


### python solution

```python
def twoStrings(s1, s2):
    # Write your code here
    s = set()
    for c in s1:
        s.add(c)
    for c in s2:
        if c in s:
            return "YES"
    return "NO"
```
### c++ solution
```c++
string twoStrings(string s1, string s2) {
    unordered_set<char> s;
    for(char c:s1) s.insert(c);
    for(char c:s2){
        if(s.find(c)!=s.end()) return "YES";
    }
    return "NO";
}
```
### analysis
- time complexity `O(n)`
- space complexity `O(n)`

## Frequency Queries
需要兩組字典
### python solution
```python
def freqQuery(queries):
    freq = dict()
    freq2num = defaultdict(int)
    ans = list()
    for (op, val) in queries:
        if op ==1:
            if val not in freq:
                freq[val] = 1
                freq2num[1]+=1
            else:
                idx = freq[val]
                freq2num[idx]-=1
                freq[val] +=1
                freq2num[idx+1]+=1
        elif op ==2:
            idx = freq.get(val,0)
            if idx==0:
                 continue
            freq[val]-=1
            freq2num[idx]-=1
            if idx-1>0:
                freq2num[idx-1]+=1
        else:
            if freq2num[val]:
                ans.append(1)
            else:
                ans.append(0)
    return ans
  
```
### analysis
- time complexity `O(n)`
- space complexity `O(n)`

