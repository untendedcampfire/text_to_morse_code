# Professional Portfolio Project - Python Scripting
# Text to Morse Code Converter
# Initial thoughts in my head, since this is just a text to morse code
# Use a Json file with morse code, downloaded from Github
# Ask user if they would like to type a string or parse a text file
# I also want it to keep running until it is told to stop

import json


def parse_text(full_file_path):
    with open(full_file_path) as f:
        text_list = f.read().split()
        text = " ".join(map(str, text_list))
        return text


def morse_coder(input_text):
    with open("morse-code.json", mode="r") as f:
        morse_code_dict = json.load(f)
    text_to_code = input_text.lower()
    morsed_list = [morse_code_dict[i] for i in text_to_code]
    morsed_code = " ".join(map(str, morsed_list))

    return morsed_code


def start_encoder():
    type_or_parse = input("Would you like to type your text or parse a file? - Enter Type or Parse: ").capitalize()

    if type_or_parse == "Type":
        coded_string = morse_coder(input("What would you like to say in morse code?: "))
        print(coded_string)

    elif type_or_parse == "Parse":
        full_file_path = input("Please enter full file path (e.g: C:/Users/User/Documents/example.txt): ")
        parsed_text = parse_text(full_file_path)
        # parsed_text = parse_text("./Secret_Text.txt")
        # print(parsed_text)
        coded_string = morse_coder(parsed_text)
        print(coded_string)

    else:
        print("Please enter a valid option")


coding_on = True

while coding_on:
    print("Welcome to the Morse Code Encoder!")
    start_encoder()
    more_morse = input("Would you like to continue? - Type Yes or No: ").lower()
    if more_morse == "yes":
        pass
    else:
        coding_on = False

