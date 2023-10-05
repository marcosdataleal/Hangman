import random

def choose_word():
    words = ['python', 'java', 'ruby', 'javascript', 'html', 'css']
    return random.choice(words)

def play_hangman(word):
    hidden_word = '_' * len(word)
    attempts = 6
    guessed_letters = []

    while '_' in hidden_word and attempts > 0:
        print(f"Current word: {hidden_word}")
        print(f"Attempts left: {attempts}")
        letter = input("Enter a letter: ").lower()

        if letter in guessed_letters:
            print("You've already guessed this letter.")
        else:
            guessed_letters.append(letter)
            if letter in word:
                print("Correct letter!")
                new_hidden_word = ''
                for i in range(len(word)):
                    if letter == word[i]:
                        new_hidden_word += letter
                    else:
                        new_hidden_word += hidden_word[i]
                hidden_word = new_hidden_word
            else:
                print("Incorrect letter.")
                attempts -= 1

    if '_' not in hidden_word:
        print(f"Congratulations! You won! The word was '{word}'.")
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    while True:
        word = choose_word()
        play_hangman(word)
        
        play_again = input("Want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

