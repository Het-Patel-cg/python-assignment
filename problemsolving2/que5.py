sen = "Hello I am HET PATEL"
short_word = 0
medium_word = 0
long_word = 0

for word in sen.split():
    if len(word) <= 3:
        short_word += 1
    elif 4 <= len(word) <= 6:
        medium_word += 1
    else:
        long_word += 1

print("Short words:", short_word)
print("Medium words:", medium_word)
print("Long words:", long_word)