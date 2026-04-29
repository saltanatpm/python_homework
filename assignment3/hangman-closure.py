def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)

        display = ""
        for ch in secret_word:
            if ch in guesses:
                display += ch
            else:
                display += "_"

        print(display)

        if all(ch in guesses for ch in secret_word):
            return True
        return False

    return hangman_closure

if __name__ == "__main__":
    secret_word = input("Enter secret word: ")
    game = make_hangman(secret_word)
    done = False
    while not done:
        guess = input("Guess a letter: ")
        done = game(guess)

    print("You guessed the word!")