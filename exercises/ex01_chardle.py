"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730465332"

cinco: str = input("Enter a 5-character word: ")

if len(cinco) != 5:
    print("Error: Word must contain 5 characters.")
    exit()

uno: str = input("Enter a single character: ")

if len(uno) != 1:
    print("Error: Character must be a single character.")
    exit()

instancia: int = 0
print("Searching for " + uno + " in " + cinco)

if cinco[0] == uno:
    print(uno + " found at index 0")
    instancia = instancia + 1
if cinco[1] == uno:
    print(uno + " found at index 1")
    instancia = instancia + 1
if cinco[2] == uno:
    print(uno + " found at index 2")
    instancia = instancia + 1
if cinco[3] == uno:
    print(uno + " found at index 3")
    instancia = instancia + 1
if cinco[4] == uno:
    print(uno + " found at index 4")
    instancia = instancia + 1

if instancia<1:
    print("No instances of " + uno + " found in " + cinco)
if instancia==1:
    print(str(instancia) + " instance of " + uno + " found in " + cinco)
else: 
    print(str(instancia) + " instances of " + uno + " found in " + cinco)