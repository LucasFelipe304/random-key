# Key Generator

This Python project generates random keys composed of letters and numbers. It offers a simple command-line interface to generate and display these keys.

## Code Structure

The code consists of the following classes and functions:

- **KeyGenerator**: Main class that generates random keys.
  - `__init__`: Initializes the alphabet for generating random letters.
  - `get_random_letter`: Returns a random letter from the alphabet.
  - `get_random_number`: Returns a random number between 0 and 9.
  - `generate_key`: Generates a key by alternating random letters and numbers.

- **display_menu**: Function that displays the main menu options.
- **close_window**: Function that displays a thank you message when the user exits the program.
- **main**: Main function that manages the program loop, handles user input, and generates keys.

## Requirements

To run this project, you will need to have Python installed on your system.

## How to Run

1. **Clone this repository**:
   ```bash
   git clone <repository URL>
   cd <repository name>

    Run the script:

    python <filename>.py

Features

    Generation of random keys composed of letters and numbers.
    Command-line interface to generate new keys or exit the program.

Usage Example

When you run the script, you will see a generated random key and the menu options:

Your random key is: a1b2c3d4e5
Options:
[1] Generate a new random key
[2] Exit

Choose the desired option to generate a new key or exit the program.