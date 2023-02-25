from intVoteCount import intVoteCount



# upper text information of the webpage
class movieInfo():
    def main_url(self):
        return "https://www.imdb.com"

    def top250_url(self):
        return "https://www.imdb.com/chart/top"

    def sublink(self, bSoup):
        return [sublink.get('href') for sublink in bSoup.select('td.titleColumn a')]

    def upperSoupText(self, subSoup):
        upperSoupText = subSoup.find('section',{"class": "ipc-page-background ipc-page-background--baseAlt sc-ccb9cf9b-0 lhZPgP"})
        return upperSoupText


    def bottomSoupText(self, subSoup):
        bottomSoupText = subSoup.find('div', {"class": "sc-f213d14f-1 ewpLoH ipc-page-grid__item ipc-page-grid__item--span-2"})
        return bottomSoupText


    def movieName(self, upperSoupText):
        try: movieName = upperSoupText.select_one('h1').text
        except: movieName = ""
        return movieName


    def movieYear(self, upperSoupText):
        try: movieYear = int(upperSoupText.find('span', {"class": "sc-f26752fb-2 eqUJdo"}).get_text(strip=True))
        except: movieYear = 0
        return movieYear


    def rating(self, upperSoupText):
        try: rating = float(upperSoupText.find('span', {"class": "sc-7ab21ed2-1 eUYAaq"}).get_text(strip=True))
        except: rating = 0
        return rating


    def voteCount(self, upperSoupText):
        vote = intVoteCount()
        try:voteCount = vote.intVoteCountTrans(upperSoupText.find('div', {"class": "sc-7ab21ed2-3 iDwwZL"}).get_text(strip=True))
        except:voteCount = 0
        return voteCount


    def director(self, upperSoupText):
        try: director = upperSoupText.find_all('div', {"class": "ipc-metadata-list-item__content-container"})[0].get_text(strip=True)
        except: director = ""
        return director


    def movieLengthMinute(self, upperSoupText):
        try: movieLengthMinute = upperSoupText.select("li")[5].get_text().split('h')[1].split(' ')[1].split('m')[0]
        except: movieLengthMinute = 0
        return movieLengthMinute


    def movieLengthHour(self, upperSoupText):
        try: movieLengthHour = upperSoupText.select("li")[5].get_text().split('h')[0]
        except: movieLengthHour = 0
        return movieLengthHour


    def movieLength(self, upperSoupText):
        movieLengthHour = self.movieLengthHour(upperSoupText)
        movieLengthMinute = self.movieLengthMinute(upperSoupText)
        if movieLengthHour[len(movieLengthHour) - 1] == "m":
            movieLengthMinute = movieLengthHour.split('m')[0]
            movieLengthHour = 0
        return int(movieLengthHour) * 60 + int(movieLengthMinute)


    def starList(self, upperSoupText):
        try:starList = upperSoupText.find_all('div', {"class": "ipc-metadata-list-item__content-container"})[2].get_text(separator=",").split(',')
        except: starList = ""
        return starList


    def gender(self, upperSoupText):
        try: gender = upperSoupText.find('div', {"class": "ipc-chip-list__scroller"}).get_text(separator=",").split(',')
        except: gender = ""
        return gender



    # bottom text information of the webpage

    def budget(self, bottomSoupText):
        try: budget = int(bottomSoupText.find_all('div', {"class": "sc-f65f65be-0 fVkLRr"})[3].select("li")[3].label.text[1::].replace(",", ""))
        except: budget = 0
        return budget


    def listDetail(self, bottomSoupText):
        try: listDetail = bottomSoupText.find('div', {"data-testid": "title-details-section"})
        except: pass
        return listDetail


    def country(self, listDetail):
        try: country = listDetail.find_all('a',{"class": "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})[1].get_text(strip=True)
        except:country = ""
        return country


    def language(self, listDetail):
        try:language = listDetail.find_all('a', {"class": "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})[4].get_text(strip=True)
        except:language = ""
        return language