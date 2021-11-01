# Open a new text file for writing
outfile = open("beer-lyrics.txt", "w")

# Iterate through 1 to 99 in reverse
for i in reversed(range(1, 100)):
    outfile.write(f"{i} botles of beer on the wall\n")
    outfile.write(f"{i} bottles of beer\n")
    outfile.write("Take one down, pass it around\n")
    outfile.write(f"{i-1} botles of beer on the wall\n")