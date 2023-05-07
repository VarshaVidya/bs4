from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,'html.parser')
tag_title = soup.select(selector=".titleline a")
for tag in tag_title:
    print(tag.string)
    print(tag.get("href"))
upvote = soup.find_all(name ="span",class_="score")
for vote in upvote:
    votes = vote.get_text().split()
    print(votes[0])

# for tag in tag_title:
#     print(tag.string)
