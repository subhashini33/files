import cx_Oracle
 
# Create a table in Oracle database
try:
 
    con = cx_Oracle.connect('system/admin@localhost:1521/xe') #1521
    print(con.version)
 
    # Now execute the sqlquery
    cursor = con.cursor()
 
    # Creating a table employee

    # cursor.execute(
    #     "create table employee(empid integer primary key, name varchar2(30), salary number(10, 2))")
 
    # print("Table Created successfully")


    # creating record in employee
    cursor.execute("insert into employee values (2,'harsh',50000)")
    con.commit()
    
    print("record inserted successfully")
    cursor.close()
    con.close
 
 
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
 
# by writing finally if any error occurs
# then also we can close the all database operation
# finally:
#     print(cursor)
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()


# from sqlalchemy import create_engine
# import pandas as pd 
# engine = create_engine('oracle://myusername:mypassword@SID')
# con = engine.connect()
# outpt = con.execute("SELECT * FROM YOUR_TABLE")
# df = pd.DataFrame(outpt.fetchall())
# df.columns = outpt.keys()
# print(df.head())
# con.close() 