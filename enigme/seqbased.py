import numpy as np
import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&%$#@"

back_chars = ".,_ "

def get_char():
   char_index = random.randint(1, len(chars)-1)
   char = chars[char_index]
   return char

def get_back_char():
   char_index = random.randint(1, len(back_chars)-1)
   char = back_chars[char_index]
   return char

###################################################################
def generate_2d_physics_puzzle():
    back_char = get_back_char()

###################################################################
def generate_sequence_puzzle():
    back_char = get_back_char()
    pat_len = random.randint(3,7)
    length = random.randint(pat_len+7,29)
    structure_1 = np.full((length), back_char)
    structure_2 = np.full((length), back_char)
    structure_3 = np.full((length), back_char)
    structure_4 = np.full((length), back_char)
    pattern = ""
    increment = random.randint(1,3)
    for i in range(0, pat_len):
        pattern = pattern +  get_char()
    start_pos = random.randint(0, length-pat_len-(3*increment))
    for i in range(0, pat_len):
        structure_1[start_pos+i] = pattern[i] 
        structure_2[start_pos+i+(1*increment)] = pattern[i] 
        structure_3[start_pos+i+(2*increment)] = pattern[i] 
        structure_4[start_pos+i+(3*increment)] = pattern[i] 
    return structure_1, structure_2, structure_3, structure_4
 
