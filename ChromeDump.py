import re
from urllib.parse import unquote

### Apologies for the regex that is about to happen....but it works so meh ###

# Office365 / Outlook format
o365user = re.compile(r'(?<=username=)(.*?)(?=&)', re.IGNORECASE)
o365pw = re.compile(r'(?<=passwd=)(.*?)(?=&)', re.IGNORECASE)

# Generic password searches
pw1 = re.compile(r'(?<="password":")(.*?)(?=,|&)', re.IGNORECASE)
pw2 = re.compile(r'(?<=password:)(.*?)(?=,|&)', re.IGNORECASE)
pw3 = re.compile(r'(?<=password=)(.*?)(?=,|&)', re.IGNORECASE)
pw4 = re.compile(r'(?<="passwd":")(.*?)(?=,|&)', re.IGNORECASE)
pw5 = re.compile(r'(?<=passwd:)(.*?)(?=,|&)', re.IGNORECASE)
pw6 = re.compile(r'(?<=passwd=)(.*?)(?=,|&)', re.IGNORECASE)
pw7 = re.compile(r'(?<=passwordtext)(.*?)\S*', re.IGNORECASE)

# Generic username searches
email1 = re.compile(r'(?<="email":")(.*?)(?=,|&)', re.IGNORECASE)
email2 = re.compile(r'(?<=email:)(.*?)(?=,|&)', re.IGNORECASE)
email3 = re.compile(r'(?<=email=)(/*?)(?=,|&)', re.IGNORECASE)
user1 = re.compile(r'(?<="username":")(.*?)(?=,|&)', re.IGNORECASE)
user2 = re.compile(r'(?<=username:)(.*?)(?=,|&)', re.IGNORECASE)
user3 = re.compile(r'(?<=username-)(.*?)(?=,|&)', re.IGNORECASE)

# Lists, because who doesn't like a list of creds
o365creds = []
genpw = []
genuser = []

# Say something!
print("Searching dump file for credentials. This may take a while.....\n")

# Get reading those dumps
with open ('dump.txt', 'rt') as dump:
    for line in dump:
        # grab those o365 creds first
        if o365user.search(line) != None:
            o365creds.append(o365user.search(line).group())
        elif o365pw.search(line) != None:
            o365creds.append(o365pw.search(line).group())
        # now for the rest of the password
        elif pw1.search(line) != None:
            genpw.append(pw1.search(line).group())
        elif pw2.search(line) != None:
            genpw.append(pw2.search(line).group())
        elif pw3.search(line) != None:
            genpw.append(pw3.search(line).group())
        elif pw4.search(line) != None:
            genpw.append(pw4.search(line).group())
        elif pw5.search(line) != None:
            genpw.append(pw5.search(line).group())
        elif pw6.search(line) != None:
            genpw.append(pw6.search(line).group())
        elif pw7.search(line) != None:
            genpw.append(pw7.search(line).group())
        # and finally usernames
        elif email1.search(line) != None:
            genuser.append(email1.search(line).group())
        elif email2.search(line) != None:
            genuser.append(email2.search(line).group())
        elif email3.search(line) != None:
            genuser.append(email3.search(line).group())
        elif user1.search(line) != None:
            genuser.append(user1.search(line).group())
        elif user2.search(line) != None:
            genuser.append(user2.search(line).group())
        elif user3.search(line) != None:
            genuser.append(user3.search(line).group())

print("Search complete....making the results a bit more presentable (maybe - there are bound to be some false positives)\n")

# Remove duplicates from the lists
o365creds = list(dict.fromkeys(o365creds))
genpw = list(dict.fromkeys(genpw))
genuser = list(dict.fromkeys(genuser))

print("\n=================\n\
Office365 Stuff\n\
=================\n") 
for i in o365creds:
    print("Raw string: " + i)  
    print("URL Decoded String: " + unquote(i))

print ("\n=================\n\
General Passwords\n\
==================\n")
for i in genpw:
    print("Raw String: " + i)
    print("URL Decoded String: " + unquote(i))

print("\n=================\n\
General Usernames\n\
===================\n")
for i in genuser:
    print("Raw String: " + i)
    print("URL Decoded String: " + unquote(i))
