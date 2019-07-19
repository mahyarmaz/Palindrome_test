word = input('write a word: ')
word_list = []
rev_list = []
for ch in word:
    word_list.append(ch)
    rev_list = word_list.copy()
    rev_list.reverse()
if rev_list == word_list:
    print('Your word is palindrome')
else:
    print('Your word is not palindrome')


