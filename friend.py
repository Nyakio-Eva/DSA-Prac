"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

input --> list of strings ==["Kariuki", "Nancy", "Ngez", "Wambui"]
output --> list of names == f"That's my friend Ngez!"

Input = ["Peter", "Stephen", "Joe"]
Output = []

constraints: 
Input string only contains letters
keep the original order of names in the output

initialize an empty list to store the names of your friend
loop through the list of strings and check if length of each is 4
if length is 4 return return the names



"""
def find_friend(s :list) -> list:
    friend = []
    for letters in s:
        if len(letters) == 4:
            friend.append(letters)
            
    return f"I found my friend {friend}!"       

print(find_friend(["Kariuki", "Nancy", "Ngez", "Wambui"]))
print(find_friend(["Peter", "Stephen", "Joe"]))