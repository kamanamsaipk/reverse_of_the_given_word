words = input("Enter the word to reverse it: ")
reversed_word = ""
i = len(words) - 1
while i >= 0:
    reversed_word += words[i]
    i -= 1

print("Reversed word is :", reversed_word)