---
title: 2487. Remove Nodes From Linked List
tags:
   - Linked List
   - monotonic stack
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/remove-nodes-from-linked-list/)

## solution
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    
    ListNode * reverse(ListNode *head)
    {
        if(!head || !head->next) return head;
        // iteratively
        ListNode * pre = nullptr, *cur = head;
        while(cur->next)
        {
            ListNode *post = cur->next;
            cur->next = pre;
            pre = cur;
            cur = post;
        }
        cur->next = pre;
        return cur;
        
    }
    
    void traverse(ListNode *head){
        while(head->next){
            cout<<head->val<<" ";
            head=head->next;
        }
        cout<<head->val<<" "<<endl;
    }
    ListNode * greater(ListNode * head){
        if(!head || !head->next) return head;
        ListNode *newhead = head, *next = newhead->next;
        while(next){
            if(next->val <  newhead->val) next=next->next;
            else{
                newhead->next = next;
                newhead=newhead->next;
                next=next->next;
            
            }
        }
        newhead->next = next;
        return head;
        
    }
    ListNode* removeNodes(ListNode* head) {
        // from right hand , the linked list is greater.
        head = reverse(head);
        traverse(head);
        // cout<<"done reverse"<<endl;
        head = greater(head);
        // traverse(head);
        // cout<<"done greater"<<endl;
        return reverse(head);
        
        
        
    }
};
```

## analysis
- time complexity `O(n)`
- space complexity `O(1)`