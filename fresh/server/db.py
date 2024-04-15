import pymysql

# PIP INSTALL PYMYSQL


db = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='cse416', charset='utf8')

cursor = db.cursor()

sql = 'select * from users'

cursor.excute(sql)

cursor.fetchall()
cursor.fetchone()
cursor.fetchmany(n)

db.commit()

db.close()