---
title: 175. Combine Two Tables
tags:  
    - Database
categories: leetcode
comments: false
---

## [problem](https://leetcode.com/problems/combine-two-tables/)

## solution
JOIN
```sql
# Write your MySQL query statement below

select a.firstName, a.lastName, b.city, b.state
from Person as a
LEFT JOIN Address as b
ON a.personId = b.personId
;
```