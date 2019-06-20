#! /usr/bin/env python3
print('Content-type: text/html\n')
import cgi
form = cgi.FieldStorage()

html ="""
<!doctype html>
<head><meta charset="utf-8"><title>Elvish Language Practice</title></head>
    <body>
        <img src={image}>
        <h2>{result}</h2>
        <h2>Try Again:</h2>

        <p>Select a word to translate:
          <select name="word">
            <option>alda</option>
            <option>amon</option>
            <option>fenume</option>
            <option>hen</option>
            <option>huo</option>
            <option>lanne</option>
            <option>lapse</option>
            <option>liikuma</option>
            <option>lunte</option>
            <option>malle</option>
            <option>meoi</option>
            <option>olva</option>
            <option>parma</option>
            <option>quaare</option>
            <option>ramba</option>
            <option>silmo</option>
            <option>taal</option>
            <option>wilin</option>
            <option>yanta</option>
            <option>yulma</option>

          </select>
          </p>

          <p>Enter your translation:<input type="text" name="guess"/></p>

          <p>
          <button type="submit">Submit</button></p>
      </form>
      </body>
      </html>"""

translated = {"baby":"lapse", "bird":"wilin", "book":"parma", "bridge":"yanta",
              "candle":"liikuma", "cat":"meoi", "cloth":"lanne", "cup":"yulma",
              "dog":"huo", "dragon":"fenume", "eye":"hen", "foot":"taal",
              "hand":"quaare", "moon":"silmo", "mountain":"amon", "plant":"olva",
              "road":"malle", "ship":"lunte", "tree":"alda", "wall":"ramba"}

elf_word = form.getfirst('word','alda')
user_input = form.getfirst('guess','')


if user_input in translated.keys():
  if elf_word == translated[user_input]:
    result = "That's correct!"
    correct_input = user_input

  else:

    for value in translated:
      if elf_word != translated[user_input]:
        result = "Sorry, the correct word was" +correct_input
        correct_input = user_input



images = "Elvish_images/" + correct_input + ".jpg"

print(html.format(image = images, result = result))
