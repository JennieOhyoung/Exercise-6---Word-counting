#Exercise 6: Files and dicts
"""Opens file in command line.
Returns counts for each time a word occurs in file"""

# import file from command line
# make empty dictionary
# open file, lowercase file
# loop through each line of file
# split by " " (tokenizing)
# if token does not yet exist, create new entry, initialize key value to 1
# if token does exist, iterate 

from sys import argv

def normalize(text):
    words = text.lower().replace("--", " ")
    wordList = words.split()
    return wordList

def main():
    script, filename = argv
    wordcount = {}

    open_file = open(filename)
    text = open_file.read()
    open_file.close()

    words = normalize(text)

    for word in words:
        word = word.strip("_,*&^@+=.!?:;-\"'")
        wordcount[word] = wordcount.get(word, 0) + 1

    print_count= []
    for key, value in wordcount.iteritems():
        print_count.append([value, key])
    
    print_count.sort(reverse = True)
    for value, key in print_count:
        print key, value

main()