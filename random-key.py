from random import randint, randrange, choice
from string import ascii_lowercase


def alphabet():
    all_letters = ascii_lowercase
    return all_letters

def numbers():
    all_numbers = randrange(start=0, stop=10)
    return all_numbers

def getting_first_letter():
    random_first_letter = choice(alphabet())
    return random_first_letter

def grouping_letter_and_number():
    key = []
    for c in range(0, 10):
      key.append(getting_first_letter())
      key.append(numbers())
    return key

def random_key(lst):
    return ''.join(map(str, lst))

def space():
   print()

def close_window():
   print('Click on "X" to close the window')

def main():
    key_list = grouping_letter_and_number()
    print(f"Your random key is: {random_key(key_list)}")
    close_window()
    while True:
      space()
      random_again = str(input("Random again? [y/n] ")).strip().lower()
      if random_again == 'y':
        key_list = grouping_letter_and_number()
        print(f"Your random key is: {random_key(key_list)}")
        close_window()
      elif random_again == 'n':
        close_window()
      else:
            print("Invalid input, please type 'y' or 'n'.")
          
if __name__ == "__main__":
   main()