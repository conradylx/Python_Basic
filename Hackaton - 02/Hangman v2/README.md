# Hangman v2
Hangman game. Before the game, the program picks random word from JSON file and display it as hidden. Then the user has to guess the password in several attempts. 

## Prerequisites

You must have the following installed:
- Python 3

### Conception of solution
Words are stored in the json file. The data is retrieved by python and originally stored in the dictionary, then the dictionary's values are converted to 
list format. The word is randomized and displayed to the user as hidden (format: '_ _ _ _' .

The hanged man is drawn in a separate window. If the password is guessed, the hanged man does not draw any further, but the password is displayed with the
message end of the game. Otherwise, the hanged man is drawn and the game is over with the password revealed. 
