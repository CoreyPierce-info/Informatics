
# import the re, urllib.request, and webbrowser module


import re, urllib.request, webbrowser

#I set the url as a variable so It would be easier to access for myself
page = "http://cgi.soic.indiana.edu/~dpierz/news.html"

#open the web page
web_page = urllib.request.urlopen(page)
contents = web_page.read().decode(errors="replace")
web_page.close()

print("Searching:", page, "\n")

#Here i opened up the the headlines and called them titles so I wouldnt get it confused.
#Then for each individual item within the title print it in the manner it was shown in the
#packet

titles = re.findall('(?<=<span itemprop="headline">).+?(?=</span>)', contents, re.DOTALL)

for title in titles:
    print("\t", title, "\n")


#Ask the user to search for a word
user_search = input("Please enter a word to search for:")

for title in titles:
    if user_search.lower() in title.lower():
        print("\t", title, "\n")
