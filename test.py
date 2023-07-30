import requests
from bs4 import BeautifulSoup
#url = "https://comic.naver.com/webtoon"
url = "https://comic.naver.com/webtoon/list?titleId=812354"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) #타이틀 가저오기
# print(soup.title.get_text()) # 타이틀 텍스트만가저오기
# print(soup.a) #가장먼저 만나는 a에대한값
# print(soup.a.attrs) # a값에대한 상세정보

#  rank1 = soup.find(attrs={"class":"EpisodeListUser__item--Fjp4R EpisodeListUser__view--PaVFx"})
# # # class가 해당이름인 엘리먼트를 찾음
# #
# # print(rank1.next_sibling.next_sibling.next_sibling) #다음엘리먼트로 이동
# # print(rank1.previous_sibling) #이전 엘리먼트로 이동
# #
# # rank1.find_next_sibling("li") # 해당 조건에 해당하는것만 찾음 li인것만 찾는다던지,
#
# rank1.find_next_siblings("li") # s를붙이면 뒤에 동일레벨을 모두가저온다


# webtoon = soup.find("a", "신혼일기")
# print(webtoon)


# cartoons = soup.find_all("a", attrs={"class": "Poster__link--sopnC"}) #해당하는 모든태그 찾기
# for cartoon in cartoons:
#     print(cartoon.get_text())


cartoons = soup.find_all("p", attrs={"class": "EpisodeListList__title_area--fTivg"})
title = cartoons.span.get_text()
print(title)
