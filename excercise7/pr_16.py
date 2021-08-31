import psycopg2
conn = psycopg2.connect(database='employeenew',user = 'jay',password = 'jay')
cr = conn.cursor()


conn.commit()
cr.close()
conn.close()