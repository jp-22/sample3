import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()
cr.execute('''alter table product add column category_id integer''')
cr.execute('''alter table product add foreign key(category_id) references category(id)''')
conn.commit()
cr.close()
conn.close()