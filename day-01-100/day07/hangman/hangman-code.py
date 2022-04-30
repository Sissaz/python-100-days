import random
import hangman_art
import hangman_words
from replit import clear

print(hangman_art.logo)
game_is_finished = False
lives = len(hangman_art.stages) - 1

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print(f"You lose. The word is {chosen_word}.")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(hangman_art.stages[lives])
    
