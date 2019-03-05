from Character import Character
from Scrapper import Scrapper
import time

# escogemos la pagina a Scrappear
character_page = "https://naruto.fandom.com/wiki/Category:Characters"
characters = []
character_objects = []

scrapper = Scrapper()

# sacamos los links de todos los personajes
while character_page is not None:

    name_box = scrapper.links(character_page)
    character_page = scrapper.nextPage
    characters = []
    character_objects = []

    for name in name_box:
        characters.append(name.get('href'))
        character_objects.append(Character(name.get('href')))

# procesamos cada link
    for character in character_objects:
        character.populate()
        time.sleep(3)


