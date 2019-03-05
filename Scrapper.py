import urllib2
import re
from bs4 import BeautifulSoup, ResultSet


class Scrapper:
    nextPage = None

    def __init__(self):
        pass

    # Scrapper de links de la lista de personajes
    def links(self, character_page):

        try:
            page = urllib2.urlopen(character_page)
        except:
            character_list = ResultSet([])
            return character_list

        soup = BeautifulSoup(page, 'html.parser')
        character_list = soup.findAll('a', attrs={'class': 'category-page__member-link'})

        nextpage = soup.find('a', attrs={'class': 'category-page__pagination-next'})

        if nextpage is None:
            self.nextPage = None
        else:
            self.nextPage = nextpage.get('href')

        return character_list

    # Scrapper del personaje individual
    def character(self, character):

        if character.url is "":
            return

        try:
            page = urllib2.urlopen("https://naruto.fandom.com" + character.url)
        except:
            return

        soup = BeautifulSoup(page, 'html.parser')

        title = soup.find('h1', attrs={'class': 'page-header__title'})
        paragraphs = soup.findAll('p');
        image = soup.find('meta', attrs={'property': 'og:image'})

        title = clean_html(title.get_text())
        image = image.get('content')
        body = ""

        for paragraph in paragraphs:

            if "Main article:" not in paragraph.get_text():
                body = body + clean_html(paragraph.get_text())

        character.title = title
        character.body = body
        character.image = image


def clean_html(raw_html):
    tags = re.compile('<.*?>')
    clean_tags = re.sub(tags, '', raw_html)

    brackets = re.compile('\[.*?\]')
    clean_brackets = re.sub(brackets, '', clean_tags)

    return clean_brackets
