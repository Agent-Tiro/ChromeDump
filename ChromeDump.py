import re
from urllib.parse import unquote

pw = re.compile(r'"password":"(.*?),', re.IGNORECASE)
email = re.compile(r'"email":"(.*?),', re.IGNORECASE)
pwd = re.compile(r'(?<=passwd=)(.*?)(?=&)', re.IGNORECASE)
passtxt = re.compile(r'PasswordText(.*?)\S*', re.IGNORECASE)
username = re.compile(r'username=(.*?)(?=,)', re.IGNORECASE)
username2 = re.compile(r'username=(.*?)(?=&)', re.IGNORECASE)
signinname = re.compile(r'signinname(.*?)\S', re.IGNORECASE)


creds = []

with open ('dump.txt', 'rt') as dump:
    for line in dump:
        if pw.search(line) != None:
            creds.append(pw.search(line).group())
        elif email.search(line) != None:
            creds.append(email.search(line).group())
        elif pwd.search(line) != None:
            creds.append(pwd.search(line).group())
        elif passtxt.search(line) !=None:
            creds.append(passtxt.search(line).group())
        elif username.search(line) != None:
            creds.append(username.search(line).group())
        elif username2.search(line) != None:
            creds.append(username2.search(line).group())
        elif signinname.search(line) != None:
            creds.append(signinname.search(line).group())

creds = list(dict.fromkeys(creds))

for i in creds:
    print("Raw string: " + i)  
    print("URL Decoded String: " + unquote(i))

