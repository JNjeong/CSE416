import pymysql

# PIP INSTALL PYMYSQL


db = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='mysql', charset='utf8')

cursor = db.cursor()

sql1 = 'show tables'
sql2 = 'select * from tb_user'

cursor.execute(sql2)

result = cursor.fetchall()
print('result : ', result)
#cursor.fetchone()
#cursor.fetchmany(n)

db.commit()

db.close()

