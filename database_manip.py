import sqlite3

#Create db file
conn = sqlite3.connect('python_programming.db')
#Execute the cursor
conn_exc = conn.cursor()
#Create the table
conn_exc.execute('''CREATE TABLE python_programming(
                     id int,
                     name text,
                     grade int
                     ) ''')
#Add rows into the table
conn_exc.execute("""INSERT INTO python_programming VALUES (55,'Carl Davis',61),
                     (66,'Dennis Fredrickson',88),
                     (77,'Jane Richards',78),
                     (12,'Peyton Sawyer',45),
                     (2,'Lucas Brooke',99)""")
#Select all records with a grade between 60 and 80.
conn_exc.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")
#Print to test
print(conn_exc.fetchall())
#Change Carl Davis’s grade to 65.
conn_exc.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")
#Delete Dennis Fredrickson’s row.
conn_exc.execute('''DELETE FROM python_programming WHERE name = "Dennis Fredrickson"''')
#Change the grade of all students, with an id greater than 55, to 80.
conn_exc.execute("UPDATE python_programming SET id = 80 WHERE id >= 55")
#commit changes
conn.commit()
#Close the database
conn.close()