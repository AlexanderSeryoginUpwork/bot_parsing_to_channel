from bs4 import BeautifulSoup
import urllib.request


class Parser:
    raw_html = ''
    html = ''
    results = []
    file = 'football.txt'

    def __init__(self, url, path=''):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('li', class_='liga-news-item')
        for item in news:
            title = item.find('span', class_='d-block').get_text(strip=True)
            description = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'description': description,
                'href': href
            })

    def save(self):
        f = open(self.file, 'w', encoding='UTF-8')
        i = 1
        for item in self.results:
            f.write(
                f"News #{i}\n\ntitle: {item['title']}\n\ndescription: {item['description']}\n\nimage: {item['href']}\n\n***************************************")

    # last
    def run(self):
        self.get_html()
        self.parsing()
        self.save()
