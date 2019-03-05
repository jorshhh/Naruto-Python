import unittest

from bs4 import ResultSet

from Scrapper import Scrapper
from Character import Character


class Testing(unittest.TestCase):
    scrapper = Scrapper()
    character = None

    # check if page doesn't exists
    def test_404(self):
        print "Testing source 404"
        url = "https://naruto.fandom.com/wiki/Category:Characters"
        links = self.scrapper.links(url)
        assert links.__class__ == ResultSet, "Should have a result set"

    def test_blank_page(self):
        print "Testing source blank page"
        url = ""
        links = self.scrapper.links(url)
        assert links.__class__ == ResultSet, "Should have a result set"

    def test_character_404(self):
        print "Testing character 404 page"
        url = "https://naruto.fandom.com/wiki/A_(First_Raikasdfasdf)"
        character = Character(url)
        character.populate()
        assert character.title is None, "Character should be empty"

    def test_character_blank(self):
        print "Testing character blank page"
        url = ""
        character = Character(url)
        character.populate()
        assert character.title is None, "Character should be empty"


if __name__ == '__main__':
    unittest.main()
