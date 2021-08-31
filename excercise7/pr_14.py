import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()

cr.execute('''select product.id,product.name,product.cost_price,product.sell_price,category.code,category.name from product inner join category on category.id = product.category_id''')
res = cr.fetchall()
print(res)

conn.commit()
cr.close()
conn.close()