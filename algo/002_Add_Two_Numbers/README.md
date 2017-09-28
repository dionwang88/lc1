### 2. Add Two Numbers
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8


### Analysis
1. Be careful the longer list, make sure to add the left part of longer list.
2. Be careful the residual
3. In the end, if the residual greater than zero, should add a new node
