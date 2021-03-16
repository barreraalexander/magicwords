from app.models.scraped_word import Scraped_Word
from app.models.my_line import MyLine
from app.utils.scrapers.webscraper import WebScraper
from app.utils.scrapers.localfilescraper import LocalFileScraper
from time import sleep

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

    def scrape_lines (self, directory):
        scraper = LocalFileScraper()
        if directory == "DRAFTS":
            lines = scraper.scrape_directory(scraper.LIT_POEMS_DRAFTS)
        else:
            lines = scraper.scrape_directory(scraper.LIT_POEMS_FINALS)

        for line in lines:
            mdict = {
                'position' : line[0][0],
                'line' : line[0][1],
                'used_in' : line[1]
            }
            new_line = MyLine(mdict)
            check = MyLine.get(by="line", value=new_line.line)
            if check:
                print ('item is already in the database')
            else:
                print ('adding new')
                MyLine.add(new_line)

    def get_sorted_words(self):
        # scraped_words = Scraped_Word.get(getall=True)
        pass
        
    def run(self):
        # scraped_words = Scraped_Word.get(getall=True)
        # for word in scraped_words:
        #     print (word.word)

        my_lines = MyLine.get(getall=True)

        position1_lines = [line for line in my_lines \
                            if line.position == 1] 
        for line in position1_lines:
            print (line)

        # lines = MyLine.get(getall=True)
        # all_words = []
        # for line in lines:
        #     all_words += line.line.split(" ")
        # # print (len(all_words))

        # for word in all_words:
        #     check = Scraped_Word.get(by="word", value=word)
        #     if not check:
        #         print ('not')
        #         try:
        #             mdict = self.webscraper.run(word)
        #             model = Scraped_Word(mdict)
        #             self.save_to_db(model)
        #             sleep(5)
        #         except Exception as err:
        #             print ("Couldn't Save to DB")
        #             print (err)

