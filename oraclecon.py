import cx_Oracle
try:
    con = cx_Oracle.connect('scott/tiger@localhost:1521/orcl')

except cx_Oracle.DatabaseError as er:
    print('There is an error in the Oracle database:', er)

else:
    try:
        cur = con.cursor() 
#create cursor
        # fetchone() is used fetch one record from top of the result set
        cur.execute('select * from emp')
        rows = cur.fetchone()
		print(rows)

    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)

    except Exception as er:
        print('Error:' + str(er))

    finally:
        if cur:
            cur.close()

finally:
    if con:
        con.close()