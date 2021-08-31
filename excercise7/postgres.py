import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()
#cr.execute('''create sequence seq_id start with 1 increment 1; ''')

#cr.execute('''create table product(id integer default nextval('seq_id'),name varchar(20) not null,cost_price integer,sell_price integer,primary key(id),check(sell_price>cost_price)) ''')

#cr.execute('''create table category(id integer,code integer unique,name varchar(20) not null,primary key(id))''')

#cr.execute('''alter table product add column category_id integer''')
#cr.execute('''alter table product add foreign key(category_id) references category(id)''')

#cr.execute('''insert into category(id,code,name) values (1,022,'hardware'),(2,033,'electronics')''')
#cr.execute('''insert into product(id,name,cost_price,sell_price,category_id) values (1,'pipe',95,110,1),(2,'tape',90,112,1),(3,'clamp',30,50,1),(4,'hook',3,5,1),(5,'door handle',90,120,1),(6,'bolt',2,5,1),(7,'knob',60,100,1),(8,'nails',3,7,1),(9,'soap holder',15,25,1),(10,'lock',200,400,1),(11,'tv',25000,30000,2),(12,'refrigerator',34000,40000,2),(13,'dvd',5000,8000,2),(14,'remoote',100,250,2),(15,'washing machine',35000,40000,2),(16,'air conditioner',25000,35000,2),(17,'mobile',95000,110000,2),(18,'mixer',3000,5000,2),(19,'hair dryer',1500,2000,2),(20,'oven',20000,23000,2)''')

# cr.execute('''select * from product ''')
# res = cr.fetchall()
# print(res)

# cr.execute('''select * from product ''')
# res = cr.fetchall()
# print(res[0])

# cr.execute('''select * from product order by cost_price''')
# res = cr.fetchall()
# print(res)

# cr.execute('''select * from product where sell_price = (select max(sell_price) from product)''')
# res = cr.fetchall()
# print(res)

# cr.execute('''update product set cost_price = 90 where id = 1''')
# cr.execute('''update product set cost_price = 85 where id = 2''')
# cr.execute('''update product set cost_price = 25 where id = 3''')

# cr.execute('''update product set sell_price = 150 where id = 1''')
# cr.execute('''update product set sell_price = 500 where id = 2''')

# cr.execute('''select * from product ''')
# res = cr.fetchall()
# print(res)

# cr.execute('''select product.id,product.name,product.cost_price,product.sell_price,category.code,category.name from product inner join category on category.id = product.category_id''')
# res = cr.fetchall()
# print(res)

conn.commit()
cr.close()
conn.close()