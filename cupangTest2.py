#광고는 제거

import requests
from bs4 import BeautifulSoup
import re
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36", 'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3'}

res = requests.get(url,headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
items = soup.find_all("li",attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:

    #광고 제거
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print("   < 광고상품 제외합니다")
        continue


    name = item.find("div", attrs={"class":"name"}).get_text()


    #애플제품 제외
    if "Apple" in name: #apple라는 글자가 name스트링안에 있으면
        print("애플 상품 제외")
        continue


    price = item.find("strong", attrs={"class": "price-value"}).get_text()


    # 4.5점이하, 50개댓글이하 제외

    rating = item.find("em", attrs={"class": "rating"})
    if rating: # none이 아니라면
        rating = rating.get_text()
    else:
        print("평점 없음 제거")
        continue

    count = item.find("span", attrs={"class": "rating-total-count"})
    if count:
        count = count.get_text()
        count = count[1:-1] # 1부터 -1까지 슬라이스 ex (34) 에서 숫자만
    else:
        print("평가 없음 제거")
        continue


    if float(rating)>= 4.5 and int(count) >= 50:
        print(name, price, rating, count)


    # rating = item.find("em", attrs={"class": "rating"})
    #
    # if rating: # none이 아니라면
    #     rating = rating.get_text()
    # else:
    #     rating = "평점 없음"

    # count = item.find("span",attrs={"class": "rating-total-count"})
    # if count:
    #     count = count.get_text()
    # else:
    #     count = "평가 없음"


