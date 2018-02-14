# 507/206 Homework 6 Part 2
import requests
from bs4 import BeautifulSoup


#### Part 2 ####
print('\n*********** PART 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Part 2 solution goes here

def part2():
    url = 'https://www.michigandaily.com/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    stufferooni = soup.find_all(class_="view view-most-read view-id-most_read view-display-id-panel_pane_1 "
                                       "view-dom-id-99658157999dd0ac5aa62c2b284dd266")
    items = stufferooni[0].find_all('li')
    for li in items:
        print(li.string)

part2()

