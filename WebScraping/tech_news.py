from bs4 import BeautifulSoup
import lxml
import requests

# The program creates 3 lists of the titles, links and the score count and turns these data into a dictionary:
# {0: {title: title, link: link, score: score} 1: {title: title, link: link, score: score} ....}
# Then prints out the news with the most upvotes from the dictionary
response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

titlelines = soup.select(".titleline")

titles = [titleline.select_one("a").getText() for titleline in titlelines]

links = [titleline.find("a")["href"] for titleline in titlelines]

# Some news doesn't have a score count so in order to don't fck up the list we firstly create a list of indexes
# that doesn't have score count. Later we insert "-1" to the scores list to the correct position
# *
subtexts = soup.select(".subtext")
nums_without_score = []
for i, subtext in enumerate(subtexts):
    i += 1
    if not subtext.find(class_="score"):
        nums_without_score.append(i)
    i -= 1

upvotes = list(map(int, [element.getText().partition(' ')[0] for element in soup.find_all(class_="score")]))
print(upvotes)
# *
for num in nums_without_score:
    upvotes.insert(num-1, -1)

# Construct the dictionary
diction = {}
for i, (title, link, upvote) in enumerate(zip(titles, links, upvotes)):
    diction[i+1] = {
        "title": title,
        "link": link,
        "upvote": upvote
    }

most_upvoted_news_index = upvotes.index(max(upvotes)) + 1
print(diction[most_upvoted_news_index])


# with open("website.html", encoding="UTF-8") as file:
#     html_text = file.read()
#
# soup = BeautifulSoup(html_text, "html.parser")
# print(soup.find_all("li"))
#
# soup.find

