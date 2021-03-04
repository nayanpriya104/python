"""
Website Blocker
-------------------------------------
"""

import time
from datetime import datetime as dt
host_path = r"/etc/hosts"
redirect = "127.0.0.1"
# you can modifiy the list of the website you want to block
web_sites_lists = ["www.facebook.com", "facebook.com"]
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("Workin Hours")
        with open(host_path, "r+") as file:
            content = file.read()
            for website in web_sites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun time")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            #reset the pointer to the top of the text file
            file.seek(0)
            for line in content:
                #here comes the tricky line, basically we overwrite the whole file
                if not any(website in line for website in web_site_list):
                    file.write(line)
                #do nothing otherwise
            file.truncate() # this line is used to remove tariling lines (that contains DNS)
    time.sleep(5)            
            
