from os import getcwd, listdir, chdir, path, walk

class LocalFileScraper:
    MAIN_LIT = '/Users/barre/main_drive/lit/'
    LIT_POEMS = path.join(MAIN_LIT, 'poems')
    LIT_POEMS_DRAFTS = path.join(MAIN_LIT, 'poems/drafts_txt')
    LIT_POEMS_FINALS = path.join(MAIN_LIT, 'poems/final_txt')
    LIT_LOGS = path.join(MAIN_LIT, 'logs')
    LIT_OBSERVATIONS = path.join(MAIN_LIT, 'observations')
    def __init__(self):
        pass

    def scrape_obs (self):
        pass

    def scrape_logs(self):
        pass

    def scrape_directory (self, directory):
        """ LIST OF POSSIBLE DIRECTORIES
        LIT_POEMS_DRAFTS
        LIT_POEMS_FINALS
         """
        chdir(directory)
        filenames = [ filename for filename in listdir() \
                    if filename[-4:] == ".txt" ]
        all_lines = []
        for filename in filenames:
            fpath = path.join(directory, filename)            

            with open(fpath, "r") as f:
                lines = [(i,line[:-1].replace("\"", "'")) \
                        for i,line in enumerate(f.readlines())]

            for line in lines:
                all_lines.append((line, filename))
        return all_lines

if __name__=='__main__':
    local_scraper = LocalFileScraper ()
