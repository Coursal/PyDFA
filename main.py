from dfa import *
from scan_input_file import *

dfa = scan_input_file("dfa.txt")

given_word = None

while given_word != '-1':
    given_word = input('Type a word (-1 to exit): ')

    if given_word == '-1':
        print('\nExiting...')
    else:
        if dfa.check_word(given_word):
            print('\tWord is valid\n')
        else:
            print('\tWord is NOT valid\n')
