#Corey Pierce
#Info I - 211
#Homework 5

#1
#[\w{6}]


#2: write an algorithm for step 3

'''
import regular expression and urllib request
open up the web page

start your lose count at zero
start your win count at zero

set variable games to re.findall to tell the program to find the schedule_game_results

for loop to find the elements within your variable "games":
    if there is a "W" in in each element:
        add 1 to the win count
    elif there is a "L" in each element:
        add 1 to the loss count

print the wins
print the losses
    


'''

#3

import re, urllib.request

web_open = urllib.request.urlopen("http://cgi.soic.indiana.edu/~dpierz/mbball.html")
contents = web_open.read().decode(errors = "replace")
web_open.close()

lose = 0
win = 0

games = re.findall("(?<=div class='schedule_game_results'><div>).*?(?=</div)", contents)

for i in games:
    if "W" in i:
        win += 1
    elif "L" in i:
        lose += 1
print("Wins:", win)
print("loses:", lose)








import re, urllib.request, webbrowser


page = "http://cgi.soic.indiana.edu/~dpierz/news.html"

web_page = urllib.request.urlopen("http://cgi.soic.indiana.edu/~dpierz/news.html")
contents = web_page.read().decode(errors="replace")
web_page.close()

print("Searching:", page,"\n")

news_article = re.findall('(?<=article class="news item).+(?=</article>)', contents, re.DOTALL)
title = re.findall('(?<=<span itemprop="headline">).+?(?=</span>)', contents, re.DOTALL)

'''
for item in title:
    if ".edu" not in title:
        print("\n", item, "\n")
'''

title_links = [item for item in title if ".edu" not in item]
print("\t", title_links, "\n")

search = input("Please enter a word to search for: ")
   

user_search = re.findall('(?<=)search.+?(?=")',title,re.DOTALL)

#url = re.findall('(?<=<h1><a itemprop="url" href=").+?(?=">)',contents,re.DOTALL)

for i in search:
    if i == user_search:
        print(word)

#webbrowser.open_new_tab(url)



























