#server.py
#  CS125 Final Project Web Interface
#  Alex Standke

# Imports
from lib.bottle import hook, response, route, run, template, static_file
import psycopg2 as pg

# Connect to db
conn_string = "host='vmwardrobe' dbname ='astandke' user='astandke' password='0424386'"
print "Connecting to database...",
conn = pg.connect(conn_string)
cursor = conn.cursor()
print "connected."

# Indexes
@route('/')
@route('/sub')
def index():
  desc = "Topics with the most subscribers:"
  cursor.execute('select count(1) as subscribers, topic_name from subscribes group by topic_name order by subscribers desc limit 20;')
  return template('index', topics=cursor.fetchall(), desc=desc)

@route('/pop')
def popular():
  desc = "Topics with the most links:"
  cursor.execute("select count(1) as links, topic_name from link group by topic_name order by links desc")
  return template('index', topics=cursor.fetchall(), desc=desc)

@route('/top')
def topular():
  desc = "Topics with the most votes:"
  cursor.execute("select count(1) as votes, link_topic from link_vote group by link_topic order by votes desc")
  return template('index', topics=cursor.fetchall(), desc=desc)  


# Topic view
@route('/t/:topic')
def topic(topic):
  cursor.execute("select sum(score) as score, link_address, headline from link left join link_vote on (address = link_address) where link_topic='"+topic+"' group by link_address, link.headline order by score desc")
  links = cursor.fetchall()
  return template('topic', topic=topic, links=links)


# Comment view
@route('/t/:topic/:address')
def comments(topic, address):
  print "select address, headline, description, user_email from link where address='"+address+"' and topic_name='"+topic+"'"
  cursor.execute("select address, headline, description, user_email from link where address='"+address+"' and topic_name='"+topic+"'")
  link = cursor.fetchall()
  print link
  cursor.execute("select user_email, contents from comment where link_topic='"+topic+"' and link_address='"+address+"'")
  comments = cursor.fetchall()
  return template('comments', link=link[0], comments=comments)


# Serve assets
@route('/assets/:filename')
def asset(filename):
  return static_file(filename, root='./assets/')


# Run like the wind
run(host='0.0.0.0', port=3030)
