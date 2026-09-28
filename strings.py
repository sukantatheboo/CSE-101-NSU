word = "COMPUTERS"
# [start : stop : step] (step ----> How many characters to jump (optional, defaults to 1))

print(word[0:4])  # Output: COMP (Grabs indexes 0, 1, 2, 3)
print(word[3:])  # Output: PUTERS (Starts at 3, goes to the end)
print(word[:4])  # Output: COMP (Starts at the beginning, stops before 4)
print(word[::2])  # Output: CMUES (Starts at beginning, goes to end, skips by 2)
print(word[::-1])  # Output: SRETUPMOC (A clever trick to reverse a string!)
print(word[::-2])

data = "apple,banana,orange"
fruits = data.split(",")  # split Breaks a string into a List based on a character
print(fruits)  # Output: ['apple', 'banana', 'orange']

# prob - 1
inp = "student@university.edu blaa"
parts = inp.split("@")  # This makes a list: ['student', 'university.edu']
print(parts[1])  # Output: university.edu

# prob - 2
# palindrome word checking
# word = input('enter a word: ')
# reverse_word = word
if word == word[::-1]:
    print(True)
else:
    print(False)

# prob - 3
inp_word = "john doe"
# final_opt = inp_word[:1].upper() + inp_word[-3:-2].upper()
# print(".".join(final_opt))
names = inp_word.split(" ")  # Makes a list: ['john', 'doe']

first_initial = names[0][0].upper()  # First word, first letter
last_initial = names[1][0].upper()  # Second word, first letter

print(f"{first_initial}.{last_initial}")

# prob - 4
# words = input("Enter a word: ")
# count = 0
# vowels = "aeiou"
# for letter in words:
#     if letter in vowels:
#         count += 1
# print(count)

# # prob - 5

inpt = "apple-banana-orange"
# print(inpt.replace('-', ' ').title())
opt = inpt.split("-")  # ['apple', 'banana', 'orange']
final_word = []
for word in opt:
    title = word[0].upper() + word[1:]
    final_word.append(title)

print(" ".join(final_word))
