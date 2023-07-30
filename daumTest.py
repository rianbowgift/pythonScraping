import requests
from bs4 import BeautifulSoup


for year in range(2015, 2020):

    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class", "thumb_img"})


    for idx, image in enumerate(images): # index에 0,1,2...식으로 넘긴
        print(image["src"])
        # image_url = image["src"]      //시작주소가 //로시작하면 주소붙여줌
        # if image_url.startswith("//"):
        #     image_url = "https:" + image_url
        #     print(image_url)

        image_res = requests.get(image["src"])
        image_res.raise_for_status()


        with open("movie{}_{}.jpg".format(year,idx+1), "wb") as f:
            f.write(image_res.content)

        if idx==4:      #상위 5개까지만 받겠음
            break