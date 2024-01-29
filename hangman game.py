#!/usr/bin/env python
# coding: utf-8

# In[28]:


import random

def check_guess():
    words = ['apple', 'orange', 'banana', 'grapes']
    return random.choice(words)

def display_guess(word, guess_word):
    display = ''
    for letter in word:
        if letter in guess_word:
            display += letter
        else:
            display += '_'
    return display

def hangman_func():
    word = check_guess()
    attempts = 6
    guess_word = set()
    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guess_word:
            print("You have already guessed that letter.")
            continue
        guess_word.add(guess)
        if guess in word:
            print("Right guess!")
            print("Word: ", display_guess(word, guess_word))
            if set(word) <= guess_word:
                print("Congratulations! You guessed the word right.")
                break
        else:
            print("Wrong guess!")
            attempts -= 1
            print("Attempts left:", attempts)
    else:
        print("Sorry, you have run out of attempts. The word was:", word)

hangman_func()


# In[ ]:





# In[ ]:




