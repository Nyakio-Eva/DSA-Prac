"""
Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

input = two lists a, b
output = list difference

examples:
if a = [1,2] and b=[1] the result would be [2]
if a = [1, 2, 2, 3] and b= [2] the result would be [1, 3]

constraints:
order of elements in the first list should be preserved ==> this means we can't use  set() to check for duplicates

note: the difference between arrays and lists is that arrays only allow one data type while lists can have different data types
 
1. the difference between two lists means elements that are present in one list but not the other.
2.loop through the two arrays , checking if items in array 1 are also present in array 2
3. initialize an empty list to store the result
4. if an item is in array 1 but not in array 2, add the item to the result.
"""
def array_diff(a :list, b :list) -> list:
    result = []
    for item in a:
        if item not in b:
            result.append(item)
    return result        

print(array_diff([1,2,3,3,4,5], [2,3]))