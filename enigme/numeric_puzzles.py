import numpy as np
import random

chars = "^*%$#@"

###################################################################
def get_char():
   char_index = random.randint(1, len(chars)-1)
   char = chars[char_index]
   return char


###################################################################
def generate_1d_numeric_text_puzzle():
    char = get_char()
    text_content = "In this block of text you will find an additional character inserted into some of the words to replace a letter. The position of this character within each word determines its numeric value, these numbers are digits in a sequence that forms a larger number. Write that number below."
    wds = text_content.split(" ")
    index = random.randint(0,int(len(wds)/3))
    answer = ""
    complete = False
    while not complete:
        word = wds[index]
        letter_index = random.randint(0,len(word)-1)
        new_word = word[0:letter_index] + char + word[letter_index+1:]
        answer += str(letter_index+1)
        wds[index] = new_word
        if (len(wds)-index) < 4:
            complete = True
        else:
            index = random.randint(index+1,len(wds)-1)
    return " ".join(wds), answer
 
def generate_1d_numeric_text_puzzle_v2():
    char = get_char()
    text_content = "In this block of text you will find an additional character inserted into some of the words to replace a letter. Each letter has a numeric value coming from its position in the alphabet, letter a is one, letter b is two, etc. Add each of these number together to get the final number. Write that number below."
    wds = text_content.split(" ")
    index = random.randint(0,int(len(wds)/3))
    answer = 0
    complete = False
    while not complete:
        word = wds[index]
        letter_index = random.randint(0,len(word)-1)
        this_char = word[letter_index:letter_index+1].upper()
        value = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(this_char)+1 
        new_word = word[0:letter_index] + char + word[letter_index+1:]
        answer += value
        wds[index] = new_word
        if (len(wds)-index) < 4:
            complete = True
        else:
            index = random.randint(index+1,len(wds)-1)
    return " ".join(wds), answer


