"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

input = array []
output = string

1. initialize an empty string to store the result
2. if array is empty display no one likes this
3. if array [0] contains a name display the name + likes this
4. if len(array) contains two names display name 1 + and + name 2 + like this
5. if len(array) contains 3 names dispaly name1 , name2 and name3 + like this
6. if len(array) contains 4 names and above, display name1, name2 +and+ len(array) - 2 + others like this

"""

def liked_items(arr: list) -> str:
    display_text = ""
    
    if len(arr) == 0:
        display_text += "no one likes this"
    
    elif len(arr) == 1:
        display_text += arr[0] + " " + "likes this"
    elif len(arr) == 2:
        display_text += arr[0] + " " + "and" + " " + arr[1] + " " + "like this"  
    elif len(arr) ==  3:
        display_text += arr[0] + "," + arr[1] + " " + "and" + " " + arr[2] + " " + "like this" 
    else:
        diff = str(len(arr) - 2)
        display_text += arr[0] + "," + arr[1] + " " + "and" + " " + diff + " " + "others like this"   
        
    return display_text

print(liked_items([]))  
print(liked_items(["Eva"])) 
print(liked_items(["Eva", "Tina"]))
print(liked_items(["Christine", "Elvis", "Noah"]))
print(liked_items(["Joyce", "Nancy", "Eva", "Winnie"]))
print(liked_items(["George", "Yusuf", "Mary", "Shirlene", "Marto", "Mbui", "Nyakio", "Grace"]))