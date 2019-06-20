#! /usr/bin/env python3
print('Content-type: text/html\n')
import cgi, MySQLdb


string = "i211s19_corepier"
password = "my+sql=i211s19_corepier"

db_con = MySQLdb.connect(host="db.soic.indiana.edu",port=3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

def update_table(cursor,item,delivery,total,shipping):
  SQL = ""
  try:
    SQL = "INSERT INTO Deliveries(Item,Cost,Method,Shipping) VALUES('"+str(item)+"','"+str(total)+"','"+str(delivery)+"','"+str(shipping)+"');"
    cursor.execute(SQL)

  except Exception as e:
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL, "Error:", e)

def print_table(cursor,item,delivery,total,shipping):
  try:
    SQL_two = "SELECT * FROM Deliveries;"
    cursor.execute(SQL_two)
    results = cursor.fetchall()

  except Exception as e:
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL_two, "Error:", e)

  else:
    result = "<table border='1' width='30%'><tr><th>Item</th><th>Cost</th><th>Method</th><th>Shipping</th></tr>"
    for row in results:
      result += '<tr>'
      for i in range(len(row)-1):
        result += '<td>'+str(row[i+1])+'</td>'
      result +='</tr>'
    result += '</table>'

  html ="""
  <!doctype html>
  <html>
  <head>
  <meta charset='utf-8'>
    <title>Robot Delivery System Confirmation</title>
  </head>
  <body>

  <h1>Robot System Delivery Confirmation</h1>
  <p>You have selected to have a {item} item delivered by
  {delivery}.</p>

  <p>Your total comes out to ${total}</p>
  <h2> Delivery Records </h2>
  {table}
  </body>
  </html>"""

  return(html.format(table = result, item = item, delivery = delivery, total = str(total+shipping)))

form = cgi.FieldStorage()

user_item = form.getfirst('item', 'unknown')
user_method = form.getfirst('delivery_method', 'Flying Drone')
user_price = form.getfirst('costs', 0)
user_price = int(user_price)

if user_method == "Flying Drone":
  shipping = 10

elif user_method == "Self Driving Car":
  shipping = 20

elif user_method == "Giant Robot":
  shipping = 1000



update_table(cursor,user_item,user_method,user_price,shipping)
db_con.commit()
print(print_table(cursor,user_item,user_method,user_price,shipping))
