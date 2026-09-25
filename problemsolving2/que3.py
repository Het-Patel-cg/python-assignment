char = "Hello!! I am Het Patel"
vowels = "aeiouAEIOU"
consonants = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
specialcharacters = "@#!"
highest_score="-1"
highest_word=""


words = char.split()

for word in words:
    score = 0
    for ch in word:
        if ch in vowels:
            score += 2
        elif ch.isalpha():
            score += 1
        elif ch.isdigit():
            score += 3
        else:
            score += 4
    print(f"word: {word}: score: {score}")
    print("highest scoring word", highest_word)
    print("score, highest_score")

