import requests
import yaml
from bs4 import BeautifulSoup
from pathlib import Path


def get_html(url: str) -> str:
    r = requests.get(url)
    return r.text


def jokes_dump(html_eng: str, html_ru: str) -> None:
    soup_eng = BeautifulSoup(html_eng, 'lxml')
    soup_ru = BeautifulSoup(html_ru, 'lxml')
    lis_eng = soup_eng.find('div', class_='content').find_all('li')
    lis_rus = soup_ru.find('div', id="article_view_-72264719_10446").find_all('li')
    joke_eng = []
    joke_rus = []
    for i in lis_eng:
        joke_eng.append(i.text)
    for i in lis_rus:
        joke_rus.append(i.text)
    with open(Path(__file__).parent / 'jokes_eng.yaml', 'w') as f:
        yaml.dump(joke_eng[:50], f)
    with open(Path(__file__).parent / 'jokes_ru.yaml', 'w') as f:
        yaml.dump(joke_rus[:50], f)


class JokeGetter:
    def __init__(self):
        self.html_eng = get_html('https://pun.me/pages/funny-jokes.php')
        self.html_rus = get_html('https://vk.com/@techrocks-top-50-shutok-programmistov-o-sebe')
        jokes_dump(self.html_eng, self.html_rus)
        with open(Path(__file__).parent / 'jokes_eng.yaml') as f:
            self.jokes_list_eng = yaml.safe_load(f)
        with open(Path(__file__).parent / 'jokes_ru.yaml') as f:
            self.jokes_list_rus = yaml.safe_load(f)
