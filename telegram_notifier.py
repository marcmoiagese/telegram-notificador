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

    keep_phrases = ["Disconnected",
                    "joined"]

    for phrase in keep_phrases:
        if phrase in txt:
            desde = '\U0001F3AE MINECRAFT SERVER: '
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={desde + txt}"
            print(requests.get(url).json())

t = tail.Tail('/home/minecraft/server/logs/latest.log')
t.register_callback(print_line)
t.follow(s=5)