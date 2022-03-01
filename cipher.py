#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Annah N Mutaya
# Created Date: 2/18/2022
# ---------------------------------------------------------------------------
# This file contains an encryption system which uses a one time pad for its cipher and returns the decrypted message
# ---------------------------------------------------------------------------

import secrets       # to generate more reliable randomness as oppossed to random
import string 
import sys

"""Function to generate the random letters of the pad. Takes in the length in characters and returns a file with random upper 
case letters of equal length"""

# msg_length = 1000       # Set a default number of characters to generate if user doesn't input message length
def generatePad(msg_length):
    pad = ""
    for index in range(msg_length):
        pad_chars = secrets.choice(string.ascii_uppercase)
        pad += pad_chars
    return pad

    # with open("pad.txt", "w") as file:       # save the result in a file called pad.txt
    #     file.write(pad)

# Function to encrypt the message. It takes in the message and the pad and returns the encrypted message.
def encipher(msg, pad):
    pad_ascii = []      # convert pad letters into ascii numbers
    for letter in pad:    
        letter_ascii = ord(letter)
        pad_ascii.append(letter_ascii)

    # shift the characters and return the shifted message in ascii
    index = 0
    shifted_msg = []
    not_ascii = []
    for char in msg:
        shift = pad_ascii[index] - 65       # Define shift as the number at index i of the pad
        if char.isalpha():
            char_ascii = ord(char) 
            if (char_ascii >= 65) and (char_ascii <= 90):
                shifted = (char_ascii - 65 + shift) % 26 + 65
            elif (char_ascii >= 97) and (char_ascii <= 122):
                shifted = (char_ascii - 97 + shift) % 26 + 97
            index += 1                      # increment the index if shifted the alpha letters
        else:
            shifted = char
            not_ascii.append(shifted)
        shifted_msg.append(shifted)
  

    # convert the ascii into letters and concatenate
    encrypted_text = ""
    letter = 0
    for i in shifted_msg:
        if i not in not_ascii:
            letter = chr(i) 
        else:
            letter = i
        encrypted_text += letter
    with open("encrypted-message.txt", "w") as file:       # save the result in a file called encrypted-message.txt
        file.write(encrypted_text)
    return encrypted_text

# Function to decrypt the encrypted message; it takes in the pad and the encrypted message, and returns the decrypted message    
def decipher(msg, pad):
    pad_ascii = []      # convert pad letters into ascii numbers
    for letter in pad:  
        letter_ascii = ord(letter)
        pad_ascii.append(letter_ascii)

    # unshift the characters and return the unshifted message in ascii
    index = 0
    decrypted_shifted_msg = []
    not_ascii = []
    for char in msg:
        shift = pad_ascii[index] - 65     # Define shift as the number at index i of the pad
        if char.isalpha():
            char_ascii = ord(char) 
            if (char_ascii >= 65) and (char_ascii <= 90):
                shifted = (char_ascii - 65 - shift) % 26 + 65
            elif (char_ascii >= 97) and (char_ascii <= 122):
                shifted = (char_ascii - 97 - shift) % 26 + 97
            index += 1                              # Increment the index of the pad if the character has been shifted
        else:
            shifted = char
            not_ascii.append(shifted)
        decrypted_shifted_msg.append(shifted)
    

    # convert the ascii into letters and concatenate
    decrypted_text = ""
    letter = ''
    for i in decrypted_shifted_msg:
        if i not in not_ascii:
            letter = chr(i) 
        else:
            letter = i
        decrypted_text += letter
    with open("decrypted-message.txt", "w") as file:       # save the result in a file called decrypted-message.txt
        file.write(decrypted_text)
    return (decrypted_text)

# Function to save the written files
def save_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)

# Prints out the command line user instructions 
def manual():
        print('1. python cipher.py -m shows a manual for how the cipher is used')
        print('2. python cipher.py -p pad.txt generates a one-time pad')
        print('3. python cipher.py -e message.txt -w pad.txt encrypts the message with the pad')
        print('4. python cipher.py -d encrypted-message.txt -w pad.txt decrypts the message with the pad')
        print()

if __name__ == '__main__':      # command line interactive tools

    cipher_choices = ["-d", "-e", "-m", "-p", "-w"]
    if len(sys.argv) == 1:
        print("Please refer to the manual below")
        manual()
    elif sys.argv[1] == cipher_choices[2]:
        print("Please refer to the manual below")
        manual()
    elif sys.argv[1] == cipher_choices[3]:
        generatePad(10000)                  # Sets a default number of characters to be generated
    elif sys.argv[1] == cipher_choices[1] and sys.argv[3] == cipher_choices[4]:
        save_file("encrypted-message.txt", encipher(sys.argv[2], sys.argv[3]))
    else:
        sys.argv[1] == cipher_choices[0] and sys.argv[3] == cipher_choices[4]
        save_file("decrpyted-message.txt",  decipher(sys.argv[2], sys.argv[4]) )