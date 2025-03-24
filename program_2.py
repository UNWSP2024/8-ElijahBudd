# Elijah Budd
#3/18/2025
# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ""
    #    Add your logic here
    new_sentence = sentence[0]

    for i in range(1, len(sentence)):
        char = sentence[i]

        if char.isupper():
            new_sentence += " " + char.lower()
        else:
            new_sentence += char

    return new_sentence.strip()

sentence = input("Enter a sentence: ")

result = word_separator(sentence)

print(result)
