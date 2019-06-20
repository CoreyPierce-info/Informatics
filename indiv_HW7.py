#! /usr/bin/env python3
print('Content-type: text/html\n')
import cgi

form = cgi.FieldStorage()
html =
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>delivery</title>
</head>
<body>

<h1><b>Robot System Delivery Confirmation</b></h1>
<p>You have selected to have a {item} delivered by
{delivery}.</p>

<p>Your total comes out to ${total}</p>

</body>
</html>

values = {"drone" : 10, "car" : 20, "robot" : 1000}
count = values[form.getfirst('delivery_method')]

for cost in form.getlist('costs'):
  count += values[cost]

print(html.format(item = form.getfirst("delivery"),
delivery = form.getfirst("delivery_method"), total = str(cost))
