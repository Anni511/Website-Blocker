import time
from datetime import datetime as dt

# Adding r before the path means we are telling Python that there are no keywords in the file path
# And that it should treat it as a raw string
hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website_list = ["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("Time To Work Boyoooo.......")
        with open(hosts_temp,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +" " +website +"\n")
            print(content)
    else:
        with open(hosts_temp,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Lets Have Some Funnnnnnn")
    time.sleep(5)
