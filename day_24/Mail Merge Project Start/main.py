#TODO: Create a letter using starting_letter.txt 

with open("./day_24/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode = 'r') as letter_file:
    letter = letter_file.read()

# print(letter)

#for each name in invited_names.txt
with open("./day_24/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
# print(names)
new_names = []

for each in names:
    space_removal = each.strip("\n")
    new_names.append(space_removal)

generated_letters = {}

for name in new_names:
    new_letter = letter.replace("[name],", name + ",")
    generated_letters[name] = new_letter

print(generated_letters)

for mails in generated_letters:
    with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_for_{mails}.docx", mode = "w") as new_files:
        new_files.write(f"{generated_letters[mails]}")

#Replace the [name] placeholder with the actual name.S
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp