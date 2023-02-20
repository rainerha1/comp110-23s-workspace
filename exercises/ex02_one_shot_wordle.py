"""EX01 - One Shot Wordle - The next step towards Wordle."""

__author__ = "730465332"

BINGO: str = "python"
guesser: str = input(f"What is your {len(BINGO)} -letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx: int = 0
emoji_house: str = ""

while len(guesser) != len(BINGO):  # guess is not the same lenth as BINGO
    guesser = (input(f"That was not {len(BINGO)} letters! Try again: "))

while idx < len(BINGO):  # while not all indices in BINGO are checked
    if guesser[idx] == BINGO[idx]:
        emoji_house = emoji_house + GREEN_BOX  # correct charcter in correct index
    else:  # not the correct character in correct index
        exists: bool = False
        a_idx: int = 0
        while not exists and a_idx < len(BINGO):
            if BINGO[a_idx] == guesser[idx]:
                exists = True
            a_idx = a_idx + 1  # checks each index in BINGO for an each index in guess
        if exists is True:
            emoji_house = emoji_house + YELLOW_BOX  # character in BINGO but wrong index
        else:
            emoji_house = emoji_house + WHITE_BOX  # character is not in BINGO
    idx = idx + 1  # checks each index in guess, loop stops after all indices are checked
print(emoji_house)  # prints green, yellow, and white boxes
if guesser == BINGO:
    print("Woo! You got it!")  # correct word
else:
    print("Not quite. Play again soon!")  # right number of characters, but incorrect word