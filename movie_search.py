import requests
from bs4 import BeautifulSoup


class MovieSearchResult:
    def __init__(self, title, year, link, img_url):
        self.title = title
        self.year = year
        self.link = link
        self.img_url = img_url

    def __str__(self):
        return f"{self.title} ({self.year})\n{self.link}\n{self.img_url}"


class MovieSearch:
    def __init__(self, query):
        self.query = query.replace(' ', '%20').replace(',', '')
        self.results = []

    async def search(self):
        self.results = await self._search_imdb()

    async def _search_imdb(self):
        imdb_url = f"https://www.imdb.com/find?q={self.query}"
        try:
            imdb_html = requests.get(imdb_url, headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
                'accept': '*/*',
                'Upgrade-Insecure-Requests': '1',
            }).text

            soup = BeautifulSoup(imdb_html, 'html.parser')
            list_names = soup.find_all('a', class_='ipc-metadata-list-summary-item__t')
            list_years = soup.find_all('li', class_='ipc-inline-list__item')

            print(len(list_names), len(list_years))
            if not list_names:
                return []

            results = []
            links = []
            years = []
            for i in range(len(list_names)):
                # movie_result = MovieSearchResult(list_names[i].text, year, link, img)

                if list_names[i].get('href').split('/')[1] == 'title':
                    links.append(f"https://www.imdb.com{list_names[i].get('href')}")
                    results.append(list_names[i].text)
                    years.append(list_years[i].text)

            print(links, "\n", results, "\n", years)

            return []

        except Exception as e:
            print(f"exception while searching IMDB for {self.query}")
            return []
