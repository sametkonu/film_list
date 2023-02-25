from tqdm import trange
import pandas as pd
from bs4 import BeautifulSoup
import requests
from links import movieInfo


class getMovieInfo():
    def movieInfo(self):
        mInfo = movieInfo()
        main_url = mInfo.main_url()
        top250_url = mInfo.top250_url()
        response = requests.get(top250_url)
        bSoup = BeautifulSoup(response.content, "html.parser")

        column_list = ["MovieSequence", "MovieName", "MovieYear", "Rating", "Director", "VoteCount", "Stars", "Genre",
                       "MovieLength", "Country", "Language", "Budget"]
        df = pd.DataFrame(columns=column_list)

        sublinks = mInfo.sublink(bSoup)

        for i in trange(0, len(sublinks)):
            sublinks[i] = main_url + sublinks[i]
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
            subResponse = requests.get(sublinks[i], headers=headers)
            subSoup = BeautifulSoup(subResponse.content, 'lxml')

            movieSequence = i + 1
            upperSoupText = mInfo.upperSoupText(subSoup)
            bottomSoupText = mInfo.bottomSoupText(subSoup)
            movieName = mInfo.movieName(upperSoupText)
            movieYear = mInfo.movieYear(upperSoupText)
            rating = mInfo.rating(upperSoupText)
            voteCount = mInfo.voteCount(upperSoupText)
            director = mInfo.director(upperSoupText)
            movieLength = mInfo.movieLength(upperSoupText)
            starList = mInfo.starList(upperSoupText)
            gender = mInfo.gender(upperSoupText)
            budget = mInfo.budget(bottomSoupText)
            listDetail = mInfo.listDetail(bottomSoupText)
            country = mInfo.country(listDetail)
            language = mInfo.language(listDetail)


            movie_dict = {'MovieSequence': movieSequence,
                          'MovieName': movieName,
                          'MovieYear': movieYear,
                          'Rating': rating,
                          'Director': director,
                          'VoteCount': voteCount,
                          'Stars': starList,
                          'Genre': gender,
                          'MovieLength': movieLength,
                          'Country': country,
                          'Language': language,
                          'Budget': budget,
                          }

            df = df.append(pd.DataFrame([movie_dict], columns=movie_dict.keys()))

        df = df.set_index(['MovieSequence'], drop=True)
        df.to_excel("filmlist.xlsx")
        return df

