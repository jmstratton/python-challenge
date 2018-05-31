


import os
import string

filename = input ('Please select which version you would like to analize (i.e paragraph_1.txt): ')

#sets file
file = os.path.join('raw_data', filename)

# open and reads file and saves text as paragraph string?
paragraph_string = ''
with open(file, 'r') as textfile:
    paragraph_string = textfile.read()


#sentence count by counting ., ? and !
sentence_count = paragraph_string.count('.') + paragraph_string.count('?') + paragraph_string.count('!')

#creates a string of upper and lowercase letters
letters = string.ascii_letters + " " 

#loops through paragraph string and deletes all characters 
# that are not letters replacing with nothing
for c in paragraph_string:
    if c not in letters:
        paragraph_string = paragraph_string.replace(c,'')


#reassigns the paragraph string and makes a list of words by splitting at spaces
paragraph_list = paragraph_string.split(" ")

#counts all of the letters in list paragraph
letter_total = 0
for word in paragraph_list:
    letter_total += len(word)

#counts words by counting the length of paragraph list
word_count = len(paragraph_list)

#calculates average word length by dividing the total # of letters
#by the number of words
avg_word_length = letter_total/word_count

# calculates words per sentence by dividing the number of words by the number of sentences.
words_per_sentence = word_count/sentence_count

PyParaText = os.path.join ('raw_data', 'ParagraphAnalysis - CHANGE ME')

#NOTE:  ***THIS FILE WILL BE OVERWRITTEN, RENAME THE FILE FOR FUTURE USE!!!!!***

with open(PyParaText, 'w') as newfile:
    newfile.write('Paragraph Analysis \n')

# opens output file and writes to it
with open(PyParaText, 'w') as newfile:

    newfile.write('Paragraph Analysis\n------------------------------\nApproximate Word Count: ' 
                        + str(word_count)+ '\nApproximate Sentence Count: '+ str(sentence_count) + 
                        '\nAverage Letter Count: ' + str(avg_word_length) + 
                        '\nAverage Sentence Length: ' + str(words_per_sentence))

# opens output file and prints to terminal
with open(PyParaText, 'r') as result_text:
    print(result_text.read())


