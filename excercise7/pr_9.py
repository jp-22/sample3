import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()

cr.execute('''select * from product order by cost_price''')
res = cr.fetchall()
print(res)

conn.commit()
cr.close()
conn.close()