import time
from datetime import datetime as dt
hosts_patht = "hosts"
hosts_pathp = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.hackerearth.com","facebook.com","www.facebook.com","www.interviewbit.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,00,00) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22,59):
        with open(hosts_pathp,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        file = open(hosts_pathp,"r+")
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()

    time.sleep(5)
