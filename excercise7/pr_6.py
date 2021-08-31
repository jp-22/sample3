import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()
cr.execute('''insert into category(id,code,name) values (1,022,'hardware'),(2,033,'electronics')''')
cr.execute('''insert into product(id,name,cost_price,sell_price,category_id) values (1,'pipe',95,110,1),(2,'tape',90,112,1),(3,'clamp',30,50,1),(4,'hook',3,5,1),(5,'door handle',90,120,1),(6,'bolt',2,5,1),(7,'knob',60,100,1),(8,'nails',3,7,1),(9,'soap holder',15,25,1),(10,'lock',200,400,1),(11,'tv',25000,30000,2),(12,'refrigerator',34000,40000,2),(13,'dvd',5000,8000,2),(14,'remoote',100,250,2),(15,'washing machine',35000,40000,2),(16,'air conditioner',25000,35000,2),(17,'mobile',95000,110000,2),(18,'mixer',3000,5000,2),(19,'hair dryer',1500,2000,2),(20,'oven',20000,23000,2)''')

conn.commit()
cr.close()
conn.close()