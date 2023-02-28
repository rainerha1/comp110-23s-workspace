"""Real Wordle Clone"""

__author__ = "730465332"

def contains_char(searched: str, the_searcher: str) -> bool:
    """Checks to see if the input character is in the word"""
    assert len(the_searcher) == 1  # assumes the_searcher is a single character
    idx: int = 0  # tracks indices
    while idx < len(searched):  # checks indices until they are all indices in searched are checked
        if searched[idx] == the_searcher:
            return True  # the_searcher is found in searched
        else:
            idx = idx + 1  # checks the next index
    return False  # the_searcher is not found in searched

def emojified(guess: str, secret: str) -> str:
    """Prints colored emojis"""
    assert len(guess) == len(secret)  # assumes the lengths of guess and secret are equal
    idx: int = 0  # tracks indices
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_house: str = ""
    while idx < len(secret):  # checks all indices in secret
        if guess[idx] == secret[idx]:
            emoji_house = emoji_house + GREEN_BOX  # correct character in correct index
            idx = idx + 1  # checks the next index
        else:
            if contains_char(secret, guess[idx]) == True:  # character is in secret
                emoji_house = emoji_house + YELLOW_BOX  # character is in secret but not in correct index
                idx = idx + 1  # checks the next index
            else:
                emoji_house = emoji_house + WHITE_BOX  # character is not in secret
                idx = idx + 1  # checks the next index
    return emoji_house  # returns list of emojis, one for each character in guess

def input_guess(expected: int) -> str:
    """Checks to see if input word is expected length"""
    guess: str = input(f"Enter a {expected} character word: ")  # asks user for an input of a certain length
    while len(guess) != expected:
        guess = (input(f"That wasn't {expected} chars! Try again: "))  # user input was not expected length
    return guess  # returns the user's input

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1  # tracks player's turns
    secret: str = "codes"  # secret word for Wordle game
    player_guess: int = len(secret)
    while turns <= 6:  # limits the player's turns to 6
        print(f"=== Turn {turns}/6 ===")  # tells the player the number turn
        code_guess: str = input_guess(player_guess)  # asks player for a word which is the length of secret
        if code_guess == secret:
            print(emojified(code_guess, secret))  # prints list of emojis for the word guessed by player
            if turns == 1:
                print(f"You won in {turns}/6 turn")  # player wins on first turn
            else:
                print(f"You won in {turns}/6 turns! ")  # player wins on any other turn
            return None
        else:
            print(emojified(code_guess, secret))  # prints list of emojis for the word guessed by player
            turns = turns + 1  # goes to next turn       
    if turns == 7:
        print("X/6 - Sorry, try again tomorrow!")  # player loses


if __name__ == "__main__":
    main()

    



