'''
Problem 22


Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
'''

def letter_value(letter):
    return ord(letter.lower())-ord('a')+1

def word_value(word):
    value=0
    for letter in word:
        value+=letter_value(letter)
    return value

content=open('022.txt').read()
names=[name[1:-1] for name in content.split(',')]
names.sort()
val=0
for pos, name in enumerate(names):
    val += (pos+1)*word_value(name)

print val