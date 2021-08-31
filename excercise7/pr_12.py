import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()

cr.execute('''update product set sell_price = 150 where id = 1''')
cr.execute('''update product set sell_price = 500 where id = 2''')
conn.commit()
cr.close()
conn.close()