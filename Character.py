from Scrapper import Scrapper
from pymongo import MongoClient


class Character:
    url = None
    title = None
    body = None
    image = None

    def __init__(self, targetUrl):
        self.url = targetUrl
        pass

    def populate(self):

        scrapper = Scrapper()
        scrapper.character(self)

        if self.title is None:
            print "Could not retrieve data for this character"
            return

        print ("populating " + self.title)

        client = MongoClient("mongodb://naruto:naruto@127.0.0.1:27017/naruto?authSource=admin")
        db = client.naruto

        characters = db.characters

        character_data = {
            'title': self.title,
            'content': self.body,
            'image': self.image,
        }

        query = characters.find({"title": self.title})

        if query.count() > 0:
            characters.update_one({"title": self.title}, {"$set": character_data})
        else:
            characters.insert_one(character_data)
