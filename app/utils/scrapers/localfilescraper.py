from os import getcwd, listdir, chdir, path, walk

MAIN_LIT = '~/main_drive/lit'
LIT_POEMS = path.join(MAIN_LIT, 'poems')
LIT_LOGS = path.join(MAIN_LIT, 'logs')
LIT_OBSERVATIONS = path.join(MAIN_LIT, 'observations')

LIT_FINAL_POEMS = path.join (MAIN_LIT, 'final_txt')


class LocalFileScraper:
    def __init__(self):
        pass

    def scrape_obs (self):
        pass


    def scrape_poems (self):
        routes = walk(top=LIT_POEMS, topdown=True)
        for step in routes:
            print (step)
            print ('\n\n')

    def scrape_logs (self):
        pass


    def run (self):
        pass

        # chdir (LIT_LOGS)
        # print (getcwd())
        print (listdir())

if __name__=='__main__':
    local_scraper = LocalFileScraper ()
    local_scraper.scrape_poems()
    local_scraper.run()
