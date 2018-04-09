"""
file: muddle.py
author: Ayush Rout
Test file: File1.txt
github: https://github.com/cloudkayl
description:
"""


def shift_space():
    """
      function shift_space: returns an integer which will be used later to shift ASCII characters 11 spaces
      :param null: no parameters, just returns int
      :return int: the ASCII Shift
    """
    return 11


def muddle(string):
    """
      function muddle: returns a string after muddling it, that is shifting the ASCII values 11 spaces to right
      :param string: (string) The plain text we want to encrypt/muddle
      :return encoding: (string) - The encrypted/muddled text
    """
    encoding = ""
    for idx in range(0,len(string)):
        encoding = encoding + chr(ord(string[idx])+shift_space())
    return encoding


def clarify(s):
    """
      function clarify: returns a string after de-muddling it, that is shifting the ASCII values 11 spaces to left
      :param s:  (string)- The encrypted string we want to de-muddle
      :return dec: (string)- The decrypted string
    """
    dec = ""
    for idx in range(0,len(s)):
        dec = dec + chr(ord(s[idx]) - shift_space())
    return dec


def input_file():
    """
    function input_file: Reads user's filename, checks for proper format, returns the file and state of contents inside that file
    :param file: the file they are writing into
    :return int: (0/1) - User input : Yes(1) ; No(0)
    """
    temp = input("Enter the file: ")
    if temp.endswith(".txt"):
        return temp, 0  #0 for plain text
    elif temp.endswith(".mud"):
        return temp, 1  #1 for muddled/encrypted text
    else:
        print("Enter a valid file type(.txt or .mud type): ")
        return "", 0    #asks again for a valid file type


def user_input(file):
    """
    function user_input: Asks the user whether they want to write to file or not(lenient about what user enters at the input promt that is
                         if prompt expects 'y', it still accepts 'Yes' and so is 'Yerba Buena!'
    :param file: the file they are writing into
    :return int: 0 or 1 for User input : Yes(1) ; No(0)
    """
    print("Enter 'y' to write results to file", file, ":", end="")
    a = input()
    a = a.lower()
    if a[0] == 'y':
        return 1
    else:
        return 0



if __name__ == "__main__":
    """
    function: main
    description: main executable code that only runs if the code is executed, and not imported
    """
    f_read = ""     #name of the file from where the data is read
    f_write = ""    #name of the file to which the data is written to
    data_in = ""    #data we are writing to the file
    data_out = ""   #data we are reading from the file
    st = 0          #format of contents of file that is 1 for encrypted/muddled and 0 for plain text

    #prompts the user to input valid file names until they are correct
    while f_read == "":
        f_read,st = input_file()

    #opens our file for reading, reads content to data_out and closes the file
    file_Read = open(f_read)
    data_out = file_Read.read()
    file_Read.close()

    #creates a file and writes to it
    if not(st): #if it is in plain text format
        f_write = f_read[0:-4] + ".mud" #uses the user's file name to create new file with .mud extension
        data_in = muddle(data_out) #obfuscate the text
    else:
        f_write = f_read[0:-4] + "_2.txt" #uses the user's file name to create new file with .txt extension
        data_in = clarify(data_out) #decrypts the obfuscated text

    if user_input(f_write):
        # if the user chooses 'y', writes new string to output file
        f_Write = open(f_write, "w") 
        f_Write.write(data_in)
        f_Write.close()
    else:
        print(data_in)


#program ends here


"""
Author: Ayush Rout
File: muddle.py
language: Python3
email: axr6077@rit.edu
"""
