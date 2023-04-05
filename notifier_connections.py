#!/usr/bin/env python

''' 
python-tail example.
Does a tail follow against /var/log/syslog with a time interval of 5 seconds.
Prints recieved new lines to standard out '''

import tail # depends of https://github.com/kasun/python-tail.git
import requests

def print_line(txt):
    
    TOKEN = ""
    chat_id = ""

    keep_phrases = ["Accepted password",
                    "New session",
                    "session closed"]

    for phrase in keep_phrases:
        if phrase in txt:
            desde = "\U0001F5A5 [SSH] MISSATGE DE SERVER: "
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={desde + txt}"
            
            print(requests.get(url).json())
           
t = tail.Tail('/var/log/auth.log')
t.register_callback(print_line)
t.follow(s=5)