import pymysql

conn = pymysql.connect('localhost', usr='CatAndTech',
                       passwd='123456', db='digimondb')
try:
    sql_command = ''
    cursor = conn.cursor()
    cursor.execute(sql_command)
except pymysql.err as e:
    print('Fail')
finally:
    cursor.close()

conn.close()
