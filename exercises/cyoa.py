"""Choose your own adventure part1."""

__author__ = "730465332"

points: int = 0
player: str
GREEN_BOX: str = "\U0001F7E9"
exists: bool = True


def main() -> None:
    global points
    global exists
    greet()
    while exists == True:
        choice: str = input("Please type chooseforme for a random guess, type mychoice to guess yourself, or type stop to end the adventure. ")
        if choice == "chooseforme":
            auto_select()
        if choice == "mychoice":
            manual_select(int(input("Choose 0 for heads or 1 for tails: ")))
        if choice == "stop":
            stoppage()
            return
        if choice != "chooseforme" and choice != "mychoice" and choice != "stop":
            choice: str = input("Please type chooseforme for a random guess, type mychoice to guess yourself, or type stop to end the adventure. ")


def greet() -> None:
    global player
    player = input("What is your name? ")
    print(f"Hello {player}, welcome to your adventure! In this this adventure, you will choose heads or tails for a coin-flip and see how many you can get right. ")


def auto_select() -> None:
    """Procedure path."""
    global points
    global player
    print(f"Alright {player}, you have chosen a blind guess. ")
    from random import randint
    bot_guess: int = randint(0,1)
    secret: int = randint(0,1)
    if bot_guess == secret:
        print(f"{GREEN_BOX}CORRECT!{GREEN_BOX}, your random guess was right. Next turn! ")
        points += 1
    else:
        print("Oops, the random guess was wrong. Try again. ")
        

def manual_select(user_guess: int) -> int:
    """Function path."""
    global points
    global player
    print(f"Ok {player}, you chose for yourself.")
    from random import randint
    secret: int = randint(0,1)
    if user_guess == secret:
        print(f"{GREEN_BOX}CORRECT!{GREEN_BOX}, you chose right! Next turn! ")
        points += 1
    else:
        print("Oops, you guessed wrong. Try again. ")
    return points


def stoppage() -> None:
    """Stop playing."""
    global points
    if points == 1:
        print(f"Your coin-flipping adventure has come to a conclusion. You ended with {points} point. ")
    else:
        print(f"Your coin-flipping adventure has come to a conclusion. You ended with {points} points. ")


if __name__ == "__main__":
    main()