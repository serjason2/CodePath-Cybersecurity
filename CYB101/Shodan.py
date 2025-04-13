# Gathering Shodan information on a given IP address
# Week 8 Project 7: Threat Analysis

import requests
import json
import re

iplist = open('iplist.txt', 'r')
lines = iplist.readlines()
output = open("shodan_out.json", "a")
for line in lines:
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    lst = []
    lst.append(pattern.search(line)[0])
    json_data = requests.get('https://internetdb.shodan.io/' + lst[0]).json()
    print(json_data)
    json.dump(json_data, output)
    output.write("\n")

iplist.close()
output.close()