sentence = 'Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення'

words = sentence.split()

print(words)

vowels = 'аеєиіїоуюя'


def replace_vowels(word):
    for char in vowels:
        word = word.replace(char, '#')
    return word


print(' '.join([replace_vowels(word) for word in words]))
