import mysql.connector as sql
db = sql.connect( host = "localhost", user = "root", password = "admin", database = "world" )
if db.is_connected():
  print('connected')
EmpCursor=db.cursor()
EmpCursor.execute('select * from country')
Data=EmpCursor.fetchone()
V_count=EmpCursor.rowcount
print('Total Rows retrieved :',V_count)
print(Data)

Data=EmpCursor.fetchall()
V_count=EmpCursor.rowcount
print('Total Rows retrieved :',V_count)
print(Data)
for i in Data:
    print(i)
  for x in range(0,14):
    print(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12])
    print(i[x])