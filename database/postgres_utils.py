import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="lecture3",
    user="postgres",
    password="postgres")

cur = conn.cursor()
res = cur.execute("select * from flights")
print(cur.fetchall())
cur.close()




from sqlalchemy import create_engine,text
engine = create_engine("postgresql://postgres:postgres@localhost:5432/lecture3")
with engine.connect() as connection:
    result = connection.execute(text("select origin from flights"))
    print(result)
    for row in result:
        print("origin:", row["origin"])




