"""
File: webcrawler.py
Name: Monica Peng
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': 't-stripe'})
        sum_male = 0
        sum_female = 0

        for tag in tags:
            trs = tag.find_all('tr')[2:202]                     # Only take from 2:202 as these contain rank 1 to rank 200 details

            for tr in trs:
                tds = tr.find_all('td')
                sum_male += int(tds[2].text.replace(',', ''))   # 3rd column is the sum of people with that Male name
                sum_female += int(tds[4].text.replace(',', '')) # 5th column is the sum of people with that Female name

        print(f'Male Number: {sum_male}')
        print(f'Female Number: {sum_female}')


if __name__ == '__main__':
    main()
