from app.application import App
from app.db import DB
from app.config import Mysql_Config
from app.utils.scrapers.webscraper import WebScraper


db = DB (config=Mysql_Config)
Scraper = WebScraper ()
def create_app ():
    app = App(db=db,
              webscraper=Scraper)

    return app