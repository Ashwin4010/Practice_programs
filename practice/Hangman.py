import random

name = input("What's your name ? ")

print("Good luck ", name)

word_list = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)

print("Guess the characters")

print(chosen_word)

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"
print(display)
print("you have 7 tries to gess the word")
end_of_game = False
lives_left = 7

while not end_of_game:

    guess = input("Guess the letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    lives_left -= 1
    print(display)
    print(stages[lives_left-1])
    if "_" not in display:
        end_of_game = True
        print("you have Won")
    elif lives_left == 0:
        print("you have lost")
        print(stages[0])
        exit()