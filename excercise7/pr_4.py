import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()
#cr.execute('''create table category(id integer,code integer unique,name varchar(20) not null,primary key(id))''')
conn.commit()
cr.close()
conn.close()
