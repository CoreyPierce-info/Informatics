#! /usr/bin/env python3
print('Content-type: text/html\n')
import cgi, MySQLdb


string = "i211s19_corepier"
password = "my+sql=i211s19_corepier"

db_con = MySQLdb.connect(host="db.soic.indiana.edu",port=3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

def buttons(cursor):
  options = []
  try:
    SQL = "SELECT * FROM Items;"
    cursor.execute(SQL)
    results = cursor.fetchall()

  except Exeption as e:
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL, "Error:", e)

  else:
    for row in results:
      options.append(row[1])
  return(options)



html = """<!doctype html>
<head><title>Robot Delivery System</title></head>
<body>
<form action='deliveryTable.cgi' method='post'>

  <h1>What would you like to have delivered?</h1>
  {content}

  <h2>Cost: $</h2>
  <input type='text' name='costs'/>

  <h2>Delivery Method:</h2>

  <br><input type='radio' name='delivery_method' value='Flying Drone'>Flying Drone ($10)
  <br><input type='radio' name='delivery_method' value='Self Driving Car'>Self Driving Car ($20)
  <br><input type='radio' name='delivery_method' value='Giant Robot'>Giant Robot ($1000)

  <p>
  <button type='submit'>Submit</button></p>
</form>
</body>
</html>"""
option_list = buttons(cursor)
content = ""

for option in option_list:
  content += """<input type='radio' name='item' value='"""+str(option)+"""'>"""+str(option)+"""<br/>"""

print(html.format(content = content))
