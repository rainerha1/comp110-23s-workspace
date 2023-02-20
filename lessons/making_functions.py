"""Shows how to write up a function"""

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

print(mimic("Hello!"))

#or

my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)

def mimic2(my_words2: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words2):
        return("Index too high")
    #If we made it here, that means the letter_idx is valid
    #Could have used an else statement, but after oen return the function stops
    return my_words2[letter_idx]

x: str = mimic2("Hi",1)
print(x)