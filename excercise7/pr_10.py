import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()
cr.execute('''select * from product where sell_price = (select max(sell_price) from product)''')
res = cr.fetchall()
print(res)


conn.commit()
cr.close()
conn.close()