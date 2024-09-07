'''
Take as input a chosen number as the height of an x-mass tree. Output a pyramid shape made up entirely of asterisks.
E.g. height = 5  will print out :
    *    
   ***  
  ***** 
 ******* 
*********

n = an integer which represents the height or number of rows on the pyramid
number of asterisks in each row = 2i+1, where i is row number starting from 0, 1, ...
use a for loop to print the rows , where i represents the current row
use the range function to print the sequence of rows with start, stop and step
print spaces to center the pyramid
spaces starting from row 0 = n-1 , row 1 = n , decreasing by 1
print asterisks

'''
n=int(input("What's the height of your x-mass tree? "))

for i in range(0,n):
    print(' ' * (n-i-1), end='')
    
    print('*' * (2*i +1))
    
    