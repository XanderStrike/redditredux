#server.py
#  CS125 Final Project Web Interface
#  Alex Standke

# Imports
import sys
from lib.bottle import hook, response, route, run, template, static_file
import psycopg2 as pg

# Connect to db
conn_string = "host='vmwardrobe' dbname ='astandke' user='astandke' password='0424386'"
def get_cursor():
  conn = pg.connect(conn_string)
  return conn.cursor()

# Indexes
@route('/')
@route('/sub')
def index():
  cursor = get_cursor()
  desc = "Topics with the most subscribers:"
  cursor.execute('select count(1) as subscribers, topic_name from subscribes group by topic_name order by subscribers desc limit 20;')
  return template('index', topics=cursor.fetchall(), desc=desc)

@route('/pop')
def popular():
  cursor = get_cursor()
  desc = "Topics with the most links:"
  cursor.execute("select count(1) as links, topic_name from link group by topic_name order by links desc")
  return template('index', topics=cursor.fetchall(), desc=desc)

@route('/top')
def topular():
  cursor = get_cursor()
  desc = "Topics with the most votes:"
  cursor.execute("select count(1) as votes, link_topic from link_vote group by link_topic order by votes desc")
  return template('index', topics=cursor.fetchall(), desc=desc)  


# Topic view
@route('/t/:topic')
def topic(topic):
  cursor = get_cursor()
  cursor.execute("select sum(score) as score, link_address, headline, id from link left join link_vote on (address = link_address) where link_topic='"+topic+"' group by id, link_address, link.headline order by score desc")
  links = cursor.fetchall()
  return template('topic', topic=topic, links=links)


# Comment view
def render_comments(comments, depth):
  cursor = get_cursor()
  html_string = ""
  for c in comments:
    html_string += "\n<div style='margin-left:" + str(depth*10) + "px' class='comment'>"
    html_string += "<font color='#bbb'>" + c[0] + "</font><p>" + c[1] + "</p>"

    cursor.execute("select user_email, contents, id from comment where parent_comment=" + str(c[2]))
    child_comments = cursor.fetchall()
    if len(child_comments) > 0:
      html_string += render_comments(child_comments, 1)
    
    html_string += "</div>"
  return html_string

@route('/t/:topic/:link_id')
def comments(topic, link_id):
  cursor = get_cursor()
  cursor.execute("select address, headline, description, user_email, topic_name from link where id='"+link_id+"' and topic_name='"+topic+"'")
  link = cursor.fetchall()
  cursor.execute("select user_email, contents, id from comment where link_topic='"+topic+"' and link_address='"+str(link[0][0])+"'")
  comments = cursor.fetchall()
  comments = render_comments(comments, 0)
  return template('comments', link=link[0], comments=comments)


# Serve assets
@route('/assets/:filename')
def asset(filename):
  return static_file(filename, root='./assets/')


# Run like the wind
if len(sys.argv) > 1:
  p = sys.argv[1] 
else:
  p = 3030
  
run(host='0.0.0.0', port=p)
