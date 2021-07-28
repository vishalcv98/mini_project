import sqlite3
import bcrypt
conn = sqlite3.connect('info.db')
c = conn.cursor()
#c.execute("""CREATE TABLE info (
        #Name text, password text)""")
i = input("Name and Password separeated by  comma ")
l = i.split(',')
l[1]=bytes(l[1], 'utf-8')
l[1]=bcrypt.hashpw(l[1],bcrypt.gensalt())
print(l)
t = tuple(l)
q="""INSERT INTO info (Name, Password ) VALUES (?, ?);"""
c.execute(q,t)
print("Success!")
conn.commit()
conn.close()