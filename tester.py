# This is where we will test the text parser from a text file
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


# def morse_coder(input_text):
#     with open("morse-code.json", mode="r") as f:
#         morse_code_dict = json.load(f)
#     input_type = type(input_text)
#     if input_type == "str":
#         text_to_code = input_text.lower()
#         morsed_list = [morse_code_dict[i] for i in text_to_code]
#         morsed_code = " ".join(map(str, morsed_list))
#     # else:
#     #     for char in input_text:
#     #         morsed_list = [morse_code_dict[i] for i in char]
#     #         morsed_code = " ".join(map(str, morsed_list))
#
#     return morsed_code

# full_file_path = input("Enter Text filepath: ")
# parsed_text = parse_text("./Secret_Text.txt")
# print(parsed_text)

coded_string = morse_coder("Hello my name's justin")
print(coded_string)


# full_file_path = input("Enter Text filepath: ")
# parsed_text = parse_text("./Secret_Text.txt")
# parsed_text
# coded_string = morse_coder(parsed_text)
# print(coded_string)

parsed_text = parse_text("./Secret_Text.txt")
print(parsed_text)
coded_string = morse_coder(parsed_text)
print(coded_string)
