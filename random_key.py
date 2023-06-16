from random import randint, choice
from string import ascii_lowercase

def randomFirstLetter():
  letters = ascii_lowercase
  randomLetter = choice(letters)
  return randomLetter


def randomKey():
  for c in range(0, 10):
    generatedKey = randomFirstLetter()
    c = randint(0, 10)
    c = str(c)
    generatedKey += c
    print(generatedKey,end='')

randomKey()
