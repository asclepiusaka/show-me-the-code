#consider the situation list is very big, so use sqlite
__author__ = 'saka'
import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE filter_list (word text)''')

with open('filtered_words.txt','r') as f:
    for line in f.readlines():
        c.execute('INSERT INTO filter_list VALUES(?)',(line.strip('\n'),))
        conn.commit()

while(True):
    word = input('please input a word: ')
    if word == 'exit':
        break
    else:
        c.execute('SELECT * FROM filter_list WHERE word=(?)',(word,))
        if c.fetchone() == None:
            print('Freedom')
        else:
            print('Human Rights')