"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

1.
2. declare an empty stack that would store opening brackets'[','(','{'. stack =  LIFO
3. loop through each character of the input string. For each character we check if it's an opening bracket, if it is we push
   it to the top of the stack
4. if it's a closing bracket, we check if the stack is empty if it is we return false. If it's not empty we check if the 
   top of the stack has an opening bracket for it, if it is we pop it from the stack otherwise we return false.   

"""
def solution(s):
    pass
        

             