from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

class WebScraper:
    #!! SCRAPE METHODS !!#
    # //SECTION: SCRAPE METHODS
    @staticmethod
    def find_rels (soup):
        """
        Returns list of related words
        Setting get_string to True returns string.
        """
        try:    
            wordscontainer = soup.findAll ("div", {"class":"css-ja4gt7 e15p0a5t0"})
            allanchors = [container.findAll ("a", {"class":"css-cilpq1 e15p0a5t1"})\
                            for container in wordscontainer]

            relatives = [elem.text.strip(",.'%{}[]()") for anchor in allanchors for elem in anchor]
        except Exception as err:
            print ('error with relatives:\n\n', err)
            relatives = 'err'

        finally:
            return relatives

    @staticmethod
    def find_pos (soup):
        """Returns part of speech"""

        try:
            poscontainer = soup.findAll ("span", {"class":"luna-pos"})
            pos = [ item.get_text().strip(",.'%{}[]()") \
                    for item in poscontainer ]
        except Exception as err:
            print ('Error with parts of speech:\n\n', err)
            pos = 'err'
        return pos


    @staticmethod
    def find_definitions (soup):
        """ returns a list of definitions """
        try:
            defscontainer = soup.findAll ("span", {"class":"one-click-content"})
            defs = [ s.get_text().strip(",.'%{}[]()") \
                    for s in defscontainer ]
        except Exception as err:
            print ('Error with definitions:\n\n', err)
            defs = 'err'
        return defs


    @staticmethod
    def find_close (soup):
        pass

    @staticmethod
    def get_search_url(search_term):
        search_url = f"""https://www.dictionary.com/browse/{search_term}?s=t"""
        return search_url

    @staticmethod
    def get_soup(search_url):
        uClient = uReq (search_url)
        pagehtml = uClient.read()
        uClient.close()

        pagesoup = soup (pagehtml, "html.parser")
        return pagesoup

    def __init__(self):
        pass
    
    def run (self, search_term):
        """ run accepts a search term
        and conducts a scrape, return a dictionary """
        search_url = self.get_search_url(search_term)
        soup = self.get_soup(search_url)
        
        #//SECTION: getting data from the soup
        rels = self.find_rels(soup)
        pos = self.find_pos(soup)
        definitions = self.find_definitions(soup)


        for i,rel in enumerate(rels):
            encode_rel = rel.encode("utf-8")
            f_rel = encode_rel.decode("utf-8", "ignore")
            rels[i] = f_rel
        
        # for i,p in enumerate(pos):
        #     encode_p = p.encode("utf-8")
        #     f_rel = encode_rel.decode("utf-8", "ignore")
        #     rels[i] = f_rel
        
        for i,definition in enumerate(definitions):
            encode_def = definition.encode("utf-8")
            f_def = encode_def.decode("utf-8", "ignore")
            definitions[i] = f_def
        

        word_dict = {
            'word' : search_term,
            'pos': "$".join(pos),
            'definitions': "$".join(definitions),
            # 'definitions': "eggs",
            'rels' : "$".join(rels),
            'syns': "none",
            'ants': "none",
            'scraped_url': search_url,
            'scraped_from' : 'dictionary.com',
        }
        return word_dict

    def __str__(self):
        return f"""
                Word: {self.searchterm}
                Part of Speech: {self.pos}
                Related Words: {self.relatives()}
                """

if __name__=='__main__':
    keyword = 'quake'
    scraper = WebScraper()
    res = scraper.run(keyword)
    print ('\n\n')
    print (res['defs'])
    # print (res['rels'])
    # print (scraper)