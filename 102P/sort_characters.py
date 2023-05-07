# Enter a line of characters, including spaces, with up to 100,000 characters.
# Sort all the characters by ASCII code increasing order from left to right
# and filter out spaces.
#
# Please note that ASCII code uses integers (0 to 255) to represent characters.
# That means, each character from input is between 0 and 255 if they are converted to integers.

# Input:
# I am a boy

characters = input()

code = []
for char in characters:
    if char == " " or char == "\t" or char == "\n" or char == "\r":
        continue  # filter out spaces
    else:
        code.append(ord(char))

code.sort()

result = ''
for code in code:
    result += chr(code)

print(result)

# Output:
# Iaabmoy