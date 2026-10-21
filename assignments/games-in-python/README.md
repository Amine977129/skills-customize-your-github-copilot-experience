# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game that lets a player guess a randomly selected word. Practice using strings, loops, conditionals, lists, and user input to track guesses and determine the outcome.

## 📝 Tasks

### 🛠️ Set Up the Game and Process Guesses

#### Description

Use the provided word list to choose a secret word, then repeatedly ask the player to guess letters and show which letters have been revealed.

#### Requirements

Completed program should:

- Randomly select one word from the predefined word list.
- Display each letter in the secret word as a blank until it is guessed, preserving the word's letter positions.
- Accept guesses without treating uppercase and lowercase versions of the same letter as different guesses.
- Reveal matching letters and keep track of incorrect guesses.

### 🛠️ Track Attempts and Finish the Game

#### Description

Limit the number of incorrect guesses and end the game when the player either reveals the full word or runs out of attempts.

#### Requirements

Completed program should:

- Set and display a maximum number of incorrect guesses, and reduce the remaining attempts for each incorrect guess.
- Continue asking for guesses while the word is incomplete and attempts remain.
- Display a clear win message when the player guesses the full word.
- Display a clear loss message and reveal the secret word when the player runs out of attempts.
