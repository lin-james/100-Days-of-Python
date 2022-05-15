# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"


with open("./Day-24-Mail-Merge/Input/Names/invited_names.txt", 'r') as invited_names:
    names = invited_names.readlines()
with open("./Day-24-Mail-Merge/Input/Letters/starting_letter.txt", 'r') as start_letter:
    letter_temp = start_letter.read()


for name in names:
    txt = name.strip("\n")
    letter = letter_temp.replace(PLACEHOLDER, txt)

    with open(f"./Day-24-Mail-Merge/Output/ReadyToSend/letter_for_{txt}.txt", 'w') as output_letter:
        output_letter.write(letter)
