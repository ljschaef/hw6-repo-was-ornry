# 507/206 Homework 6 Part 1
from bs4 import BeautifulSoup
import requests
import sys

#### Part 1 ####
print('\n*********** PART 1 ***********')
print("Mark's page -- Alt tags\n")

### Your Part 1 solution goes here

def part1():
    url = sys.argv[1]
    html = url
    got_get = requests.get(str(html)).text
    text = BeautifulSoup(got_get, 'html.parser')
    images = text.find_all('img')
    for a in images:
        try:
            a['alt']
            print(a['alt'])
        except:
            print("No alternative text provided!")

part1()


