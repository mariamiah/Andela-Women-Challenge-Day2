# Prompt User to enter any word
word = input("Enter a word: ")


def countVowels(word):
    ''' Function that returns vowels from original string'''
    vowels = ['a', 'e', 'i', 'o', 'u']
    duplicates = len(word) - len(set(word))
    return ''.join(letter for letter in word if letter in vowels), duplicates

print(countVowels(word))
