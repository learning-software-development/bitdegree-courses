print('Welcome to the Pig Latin Translator!')

pyg = 'ay'

original = input('Enter a word: ')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:] + first + pyg
    print(new_word)
else:
    print('Empty')
