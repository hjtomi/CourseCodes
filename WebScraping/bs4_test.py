from bs4 import BeautifulSoup
import requests
import urllib.request


# response = requests.get("https://onvideo.hu/video/2134/harry-potter-es-a-halal-ereklyei-1-resz-online-teljes-film-magyarul/")
# web_html = response.text
#
#
# soup = BeautifulSoup(web_html, "html.parser")
#
# sources = soup.find_all(name="source")
# print(sources)

urllib.request.urlretrieve("https://data2.onvideo.hu/halalereklyei.mp4", "halalereklyei.mp4")

