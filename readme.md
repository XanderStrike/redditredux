Link Sharer Deleuexuee
======================

Alexander Standke

CS125: Database Design

  This is a super simplistic implementation of [Reddit](http://www.reddit.com) or [Hacker News](http://news.ycombinator.com). Due to laziness, time constrains, and the difficulty of rolling a session manager from scratch, it is actually just a viewer for the database we were asked to design. I considered using Rails or Sinatra with ActiveRecord or some other object-relational mapping library, which would have allowed me to use libraries I am familiar with to manage user sessions, but thought that would be contrary to the spirit of the assignment as I could have written the whole thing without a single line of SQL.

  I decided to challenge myself and use a very simple framework that I had limited experience with, [bottle.py](http://bottlepy.org/docs/dev/). I hoped when I made this decision to be able to leverage [Cork](http://cork.firelet.net/), a simple auth library for Bottle, for user sessions. However, getting it to play nice with psycopg2 proved beyond my abilities in the time allotted.

Usage
-----

* Be on linux
* Be somewhere you can access vmwardrobe
* Install psycopg2: `apt-get install python-psycopg2`
* `python server.py`

This will start it listening on port 3030. If you want to use a different port, just add it as an argument (i.e. `python server.py 5678`).
