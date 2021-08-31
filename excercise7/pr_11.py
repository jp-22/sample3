import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()
cr.execute('''update product set cost_price = 90 where id = 1''')
cr.execute('''update product set cost_price = 85 where id = 2''')
cr.execute('''update product set cost_price = 25 where id = 3''')
conn.commit()
cr.close()
conn.close()