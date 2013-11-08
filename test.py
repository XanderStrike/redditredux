import psycopg2 as pg
import sys
import pprint

conn_string = "host='vmwardrobe' dbname ='astandke' user='astandke' password='0424386'"

print "Connecting to database \n%s" % (conn_string)

conn = pg.connect(conn_string)

cursor = conn.cursor()

print "Connected"

cursor.execute("SELECT name FROM topic")

records = cursor.fetchall()

pprint.pprint(records)
