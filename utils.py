import json
import time
from bs4 import BeautifulSoup
import requests
import textwrap


def scrape(request):
    start_time = time.time()
    headlines = []
    articles = []

    for i in range(3):
        r = requests.get("https://dailypost.ng/hot-news/page/{}".format(i))
        soup = BeautifulSoup(r.content, "html.parser")
        mydivs = soup.findAll("span", {"class": "mvp-cd-date left relative"})
    for div in mydivs:
        mytags = div.findNext('h2')
        for tag in mytags:
            headlines.append(tag.strip())

    z = [linkk.get('href', '/') for linkk in soup.find_all("a", {"rel": "bookmark"})]
    for url in z:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        conteent = soup.find(id="mvp-content-main")
        article = ''
        line_size = 80
        for i in conteent.findAll('p'):
            w = textwrap.TextWrapper(width=line_size, break_long_words=False, replace_whitespace=False)
            body = '\n'.join(w.wrap(i.text))
            article += body + "\n\n"
        articles.append(article)
    
    articles_data=[]
    id=list(range(1,len(headlines)+1))
    for i in range(len(headlines)):
        d={
            "id":id[i],
            "title":headlines[i],
            "content":articles[i]
        }
        articles_data.append(d)

    data = json.dumps(articles_data)
    print(data)
    print("--- %s seconds ---" % (time.time() - start_time))
    return data


scrape(1)
