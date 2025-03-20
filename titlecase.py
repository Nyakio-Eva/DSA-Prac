"""Your function should take a string as an input and convert all the first letters of the words in the string to uppercase, making the string a title case (other letters must be in lowercase).
How it’s used:

for text processing and data normalization tasks;
for rendering text in UI in a standard title case format.
Preconditions:

sentence ∈ string;
length(sentence) >= 0.

Examples
assert to_title_case("hello world") == "Hello World"
"""
def to_title_case(sentence :str) -> str:
    words = sentence.split()
    title_case_words = []
    
    for word in words:
        capitalized = word.capitalize()
        title_case_words.append(capitalized)
        
    return " ".join(title_case_words)   

print(to_title_case("hello classroom? how is your day going?"))