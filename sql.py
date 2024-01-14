import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()
# Drop the table if it exists


# table_info = """CREATE TABLE STUDENT (
#     NAME VARCHAR(25),
#     CLASS VARCHAR(25),
#     SECTION VARCHAR(25),
#     MARKS INT
# );
# """

# cursor.execute(table_info)

# Queries to INSERT records.
cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C', 75)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C', 92)''')

# Display data inserted
print("Data Inserted in the table:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()

# Closing the connection
connection.close()
