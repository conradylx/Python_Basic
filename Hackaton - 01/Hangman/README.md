# Hangman
Hangman game. Before the game, you can choose the category from which the question will be drawn. Then the user has to guess the password. 

## Prerequisites

You must have the following installed:
- Python 3

### Conception of solution
Categories with words are stored in the json file. The data is retrieved by python and stored in the dictionary, then the word 
is randomized and displayed to the user as hidden. 
After x attempts it is displayed that the password has been guessed or the whole password is displayed - if it is not guessed.
