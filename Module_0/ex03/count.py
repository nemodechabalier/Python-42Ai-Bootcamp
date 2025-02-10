import sys
import string

def text_analyser(text):

    num_upper = 0
    num_lower = 0
    num_punc = 0
    num_space = 0
    
    for char in text:
        if char.isupper():
            num_upper += 1
        elif char.islower():
            num_lower += 1
        elif char in string.punctuation:
            num_punc += 1
        elif char.isspace():
            num_space += 1
    
    print("- ", num_upper, " upper letter(s)")
    print("- ", num_lower, " lower letter(s)")
    print("- ", num_punc, " punctuation mark(s)")
    print("- ", num_space, " space(s)")

argument = sys.argv[1:]

if len(argument) == 1:
    text_analyser(argument[0])
