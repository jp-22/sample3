import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()
cr.execute('''create sequence seq_id start with 1 increment 1; ''')

cr.execute('''create table product(id integer default nextval('seq_id'),name varchar(20) not null,cost_price integer,sell_price integer,primary key(id),check(sell_price>cost_price)) ''')

conn.commit()
cr.close()
conn.close()