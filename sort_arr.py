"""
- array of unsorted integers.
- implement a function to find the second-largest number in the array without using built in sorting functions
input: arr = [12,34,56,78,90,23,45,67]
output: 78

1.initialize an empty array to store the sorted numbers
2.use a while loop through the array to find the largest number using the max function
3.store it in a variable
4.append max value to the sorted numbers array
5.remove max value from the input array
6.return the number at index one [1]

"""
def sort_func(arr: list) -> list:
    sorted_arr = []
    
    while arr:
        max_num = max(arr)
        sorted_arr.append(max_num)
        arr.remove(max_num)
        
    return sorted_arr[1]

print(sort_func([12,34,56,78,90,23,45,67]))  