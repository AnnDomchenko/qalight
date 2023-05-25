sentence = 'Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення'

words = sentence.split()

print(words)

vowels = 'аеєиіїоуюя'


def replace_vowels(word, skip):
    if not word.lower().startswith(skip.lower()):
        for char in word:
            if char in vowels:
                word = word.replace(char, '#')
    return word


print(replace_vowels())
