import sqlite3

conn = sqlite3.connect("code.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE codes (
            num INT PRIMARY KEY,
            code CHAR(36))''')

with open("record.txt","r") as f:
    content = f.readlines()
    for i,line in enumerate(content):
        cur.execute('''INSERT INTO codes VALUES 
        (?,?)''',(i,line.strip("\n")))
        conn.commit()

conn.close()



