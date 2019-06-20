#! /usr/bin/env python3
print('Content-type: text/html\n')
import MySQLdb, cgi

#logging into the MySQL
string = "i211s19_corepier"
password = "my+sql=i211s19_corepier"

db_con = MySQLdb.connect(host="db.soic.indiana.edu",port=3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

#This returns the HTML
def print_table(cursor):
#Selects all of the song in Songs table
  try:
    SQL = "SELECT * FROM Songs;"
    cursor.execute(SQL)
    results = cursor.fetchall()
#If it doesnt Run
  except Exception as e:
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL, "Error:", e)

  #this is where we create the table
  else:
    result ="<table border='1' width='50%'><tr><th>SongID</th><th>Song</th><th>Artist</th><th>Price</th><th>Buy</th></tr>";
    for row in results:
      result += '<tr>'
      for item in row:
        result += "<td align='center'>"+str(item)+"</td>"

      result += "<td><a href='Sold.cgi?song=" + str(row[0]) + "'>Buy</td>"
    result += '</table>'

#The HTml with the table included
  html = """
  <!doctype html>
  <html>
  <head><meta charset="utf-8"><title>Tune Shop</title></head>
  <body><h1>Welcome to the Tune Shop</h1>
    {table}
  </body>
  </html>"""

  return(html.format(table = result))
print(print_table(cursor))
