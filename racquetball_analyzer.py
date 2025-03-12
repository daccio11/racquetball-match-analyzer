import re

# Open the input file for reading, prompting the user for the filename
inputfile = open(input("Enter file name:"), "r")

# Initialize empty lists and variables
names = []  # List to store extracted characters
names2 = ''  # String to store formatted names with spaces
scores = []  # List to store extracted name-score pairs
user1Score = 0  # Total score for first detected player
user2Score = 0  # Total score for second detected player

# Read the first line of the file and store it as a string
stringPlayer = str(inputfile.readline())

# Iterate over each character in the string
for char in stringPlayer:
    names.append(char)  # Append character to names list

    # If the character is '1' or '2', insert a space to separate names from scores
    if char == '1' or char == '2':
        names.append(" ")

# Convert list back to a string
for char in names:
    names2 += char

# Split the formatted string into a list of names and scores
names3 = names2.split()

# Use regex to extract names and associated scores
for i in names3:
    match = re.match(r"([a-z]+)([0-9]+)", i, re.I)  # Match name (letters) and score (digits)
    if match:
        items = match.groups()  # Extract matched groups (name, score)
        scores.append(items)  # Append extracted data to scores list

# Identify players based on first detected names in the score list
user1 = scores[0][0]  # First player's name
for n in scores:
    if n[0] != user1:
        user2 = n[0]  # Identify second player

# Calculate total scores for each player
for n in scores:
    if n[0] == user1:
        user1Score += int(n[1])
    if n[0] == user2:
        user2Score += int(n[1])

# Determine and print the winner
if user1Score > user2Score:
    print(f"{user1} wins with {user1Score} points!")
if user2Score > user1Score:
    print(f"{user2} wins with {user2Score} points!")
