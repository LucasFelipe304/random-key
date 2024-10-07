from random import choice, randrange
from string import ascii_lowercase

class KeyGenerator:
    def __init__(self):
        """Initializes the alphabet for generating random letters."""
        self.alphabet = ascii_lowercase

    def get_random_letter(self):
        """Returns a random letter from the alphabet."""
        return choice(self.alphabet)

    def get_random_number(self):
        """Returns a random number between 0 and 9."""
        return randrange(10)

    def generate_key(self):
        """Generates a key by alternating random letters and numbers."""
        key = []
        for _ in range(10):  # Generates a sequence of 10 letter-number pairs
            key.append(self.get_random_letter())
            key.append(self.get_random_number())
        return ''.join(map(str, key))  # Joins the list elements into a string

def display_menu():
    """Displays the main menu options."""
    print("\nOptions:")
    print("[1] Generate a new random key")
    print("[2] Exit")

def close_window():
    """Prints a message when the user chooses to exit the program."""
    print('Thank you for using the key generator!')

def main():
    """Main loop of the program, handles user input and generates keys."""
    generator = KeyGenerator()
    
    while True:
        print(f"\nYour random key is: {generator.generate_key()}")  # Generate and display key
        display_menu()
        
        option = input("Choose an option: ").strip().lower()  # Handles user input
        
        if option == '1':
            continue  # Continue loop to generate a new key
        elif option == '2':
            close_window()
            break  # Exit the program
        else:
            print("Invalid input. Please enter '1' to generate a new key or '2' to exit.")  # Error feedback

if __name__ == "__main__":
    main()
