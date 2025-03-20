"""
This function should take three strings as input: the main text, the target substring, and the replacement substring. It should return a new string where all occurrences of the target substring within the main text are replaced with the replacement substring.

How its used:
in text editors for find-and-replace functionality;
in data transformation tools to standardize or clean data;
in website template systems to replace placeholders with actual content.

constraints:
all inputs should be strings: mainText, target, replacement ∈ string;
the target should not be an empty string: length(target) > 0.

use .replace(old,new, count) method
main_text.replace(target_text, replacement)

"""
def replace_all(main_text: str, target_text: str, replacement: str) -> str:
    replaced_text = main_text.replace(target_text,replacement)
    return replaced_text

print(replace_all("I love using world", "world", "Python"))