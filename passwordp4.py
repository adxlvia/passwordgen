import random
import string
import requests

# function that generates a single random character
def random_character():
    choices = string.ascii_letters +string.digits + string.punctuation
    return random.choice(choices)

passwordLength = int(input("How long would you like your password to be?"))

# function that generates a random password
def generate_strong_password():
    password = ""
    for i in range(passwordLength):
        password = password + random_character()
    print(password)

generate_strong_password()

# function to give us a random word
def fetch_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?length=6")
    word = response.json()[0]
    return word

def replaceLetters(word):
    word = word[0].upper() + word[1:]

    if "a" in word:
        word = word.replace("a", "@")
    if "e" in word:
        word = word.replace("e", "3")
    if "l" in word:
        word = word.replace("l", "!")
    if "s" in word:
        word = word.replace("s", "$")

    return word
    
    def generate_weaker_password():
        word1 = fetch_word()
        word2 = fetch_word()
        word1 = replaceLetters(word1)
        password = word1 + word2
        return password


print(fetch_word())
