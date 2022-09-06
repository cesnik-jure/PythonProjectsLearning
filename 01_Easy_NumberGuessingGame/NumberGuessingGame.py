def main():
    import random

    guess_number = random.randrange(0, 10, 1)
    guess_user = int(input("Guess a number between 0 and 10: "))

    while guess_number != guess_user:
        print("The number is not correct.")
        if guess_number > guess_user:
            print("Try a higher number.")
            guess_user = int(input("Guess again: "))
        elif guess_number < guess_user:
            print("Try a lower number.")
            guess_user = int(input("Guess again: "))
        else:
            break

    print("You guessed the correct number!")


if __name__ == '__main__':
    main()
