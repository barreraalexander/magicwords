from app.models.scraped_word import Scraped_Word
from app.models.scraped_word import Scraped_Word
from app.utils.scrapers.webscraper import WebScraper
from app.utils.scrapers.localfilescraper import LocalFileScraper

class App:
    def __init__ (self, db=None, webscraper=None):
        self.db = db
        self.webscraper = webscraper
    
    @staticmethod
    def word_handler (word):
        """ modifies the word dict and adds it to the database """
        pass


    def deep_dive (self):
        all_words = Scraped_Word.get(getall=True)
        for elem in all_words:
            terms = elem.rels.split('$')
            scraper = WebScraper()
            for term in terms:
                try:
                    mdict = scraper.run(term)
                    model = Scraped_Word(mdict)
                    self.save_to_db(model)
                except:
                    pass

    def save_to_db (self, model):
        try:
            Scraped_Word.add(model)
            print (f'saved {model.word}')
        except Exception as err:
            print (err)
            model.definitions = 'none'
            print ('\n\ndefinition set to none')
            try:
                Scraped_Word.add(model)
                print('added model with no definition')
            except Exception as err:
                print ('could not add model')

    def get_all_rels (self):
        words = Scraped_Word.get(getall=True)
        rels = []
        for elem in words:
            elem_rels = elem.rels.split('$')
            rels += elem_rels
        return rels
        
    def run(self):
        # rels = self.get_all_rels()
        # print (rels)
        scraper = LocalFileScraper()
        scraper.run()
