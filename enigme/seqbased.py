import numpy as np
import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&%$#@"

def get_char():
   char_index = random.randint(1, len(chars)-1)
   char = chars[char_index]
   return char

###################################################################
def generate_sequence_puzzle():
    back_char = "_"
    pat_len = random.randint(3,7)
    length = random.randint(pat_len+5,16)
    structure_1 = np.full((length), back_char)
    structure_2 = np.full((length), back_char)
    structure_3 = np.full((length), back_char)
    structure_4 = np.full((length), back_char)
    pattern = ""
    for i in range(0, pat_len):
        pattern = pattern +  get_char()
    start_pos = random.randint(0, length-pat_len-2)
    for i in range(0, pat_len):
        structure_1[start_pos+i] = pattern[i] 
        structure_2[start_pos+i+1] = pattern[i] 
        structure_3[start_pos+i+2] = pattern[i] 
        structure_4[start_pos+i+3] = pattern[i] 
    return structure_1, structure_2, structure_3, structure_4
 
