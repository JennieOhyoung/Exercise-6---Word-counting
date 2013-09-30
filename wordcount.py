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

def main():
    script, filename = argv
    wordcount = {}

    open_file = open(filename)
    text = open_file.read()
    words = text.lower().split()
    open_file.close()

    #splitting by space going line by line

    for word in words:
        wordcount[word] = wordcount.get(word, 0) + 1
        print word, wordcount[word]

main()