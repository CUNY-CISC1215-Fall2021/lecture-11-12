import random

# Open the book for reading
infile = open('jane_eyre.txt', 'r')

# A list containing all the words in the input text in order
words = []

# First pass: Assemble the word list.
# To do this, we start by iterating over every line in the book
for line in infile:
    # Preprocessing: Lowercase, strip whitespace, and split with
    # spaces as a delimiter
    #
    # Other optional steps to consider: remove quotes (") and
    # dashes (-) since they are used frequently in this book
    line = line.strip().lower()
    line = line.split(' ')

    #Iterate through each word in the line
    for word in line:
        # If the word is an empty string, ignore it
        if not word:
            continue

        # Otherwise, append to our words list
        words.append(word)

# Second pass: do a Markov analysis on the words in the book 
analysis = {}

# Iterate over the indices of all our words, with the exception of the last
for i in range(len(words)-1):
    # If we have never encountered a word before, add it to the analysis dict
    if words[i] not in analysis:
        analysis[words[i]] = []
    
    # Add the word following this word (the suffix) to the list of all possible
    # candidate suffixes for this word
    analysis[words[i]].append(words[i+1])

# Text generation step

# First, choose an initial prefix at random
prefix = random.choice(list(analysis.keys()))

# Create a list of output words and add our initial prefix
output = [prefix]

# Generate a sentence of 100 words
for i in range(100):
    # Choose a random suffix from the list of candidate suffixes
    choice = random.choice(analysis[prefix])

    # Remember our choice, and make the chosen suffix the new prefix
    output.append(choice)
    prefix = choice

# Final output
print(' '.join(output))