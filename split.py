"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

examples:
'abc' => ['ab','c_']
'abcdef' => ['ab', 'cd', 'ef']


1. use slice(::2) method to split characters in pairs => use range to loop while slicing
2. check if the last character has a pair using if i + 1 < len(s) 
3. i would be the current position in the string which is increased by 2 in each loop iteration
4.i + 1 would be the position of the second character in the potential pair 
5. len(s) is the length of the string
6. so i + 1 < len(s) checks if the position i + 1 is still within the bounds of the string if so, the slicing happens else the '_ ' character is added to the end 


"""
def split_string(s :str) -> str:
    paired_letters = []
    
    for i in range(0, len(s), 2):
        if i + 1 < len(s):  #checks if the last character has a char to pair with
            pairs = s[i:i +2]
        else:   
            pairs = s[i] + '_'
        
        paired_letters.append(pairs)
        
    return paired_letters   

        
    
print(split_string("abcde"))    