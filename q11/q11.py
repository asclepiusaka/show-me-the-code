__author__='saka'

filtered_list = set()
with open('filtered_words.txt','r') as f:
    for line in f.readlines():
        filtered_list.add(line.strip('\n'))

while(True):
    word = input('please input a word: ')
    if word == 'exit':
        break
    elif word in filtered_list:
        print('Human Rights')
    else:
        print('Freedom')
