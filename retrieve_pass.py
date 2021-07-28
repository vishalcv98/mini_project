import sqlite3
import bcrypt
conn = sqlite3.connect('info.db')
c = conn.cursor()
i = input("Enter your UserName")
j = input("Enter your Password")
j = bytes(j, 'utf-8')
try:
    c.execute('SELECT password from info WHERE Name = (?)',(i,))
except:
    print("Username doesn't exist")
enc = (c.fetchone()[0])
if bcrypt.checkpw(j , enc):
    print("Success")
    print("Enter new Username and password separated by comma")
    k = input()
    l=k.split(',')
    c.execute('UPDATE info SET NAME = (?) WHERE Name = (?)' , (l[0],i))
    c.execute('UPDATE info SET password = (?) WHERE Name = (?)', (l[1], i))
else:
    print("Wrong Password")

conn.commit()
conn.close()