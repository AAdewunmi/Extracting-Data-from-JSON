#Extracting Data from JSON
#The program will prompt for a URL, read the JSON data from that URL using urllib
#and then parse and extract the comment counts from the JSON data,
#compute the sum of the numbers in the file.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Sample Execution

#$ python3 solution.py
#Enter URL: http://py4e-data.dr-chuck.net/comments_42.json
#Retrieving http://py4e-data.dr-chuck.net/comments_42.json
#Retrieved 2733 characters
#Count: 50
#Sum: 2...

import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter URL: ")
print("Retrieving ", url)

uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
total = 0
print("Retrieved: ",len(data),"characters")
print("Count: ", len(info["comments"]))

for i in range(0, len(info["comments"])):
    total += int(info["comments"][i]["count"])
print("Sum", total)
