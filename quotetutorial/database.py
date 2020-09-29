import sqlite3

conn = sqlite3.connect("myquotes.db")
curr = conn.cursor()

# curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
# curr.execute("""create table quotes_tb ( title , author ,tag)""")
# curr.execute(f"insert into quotes_tb ( title , author ,tag) values( {item['title'][0]},{item['author'][0]},{item['tag'][0]})")
title = "python"
author = "rdx"
tag = "new"

curr.execute("""insert into quotes_tb values('python','rdx','new' )""")

conn.commit()
conn.close()