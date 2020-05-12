from bs4 import BeautifulSoup
import requests
import random


def Movies_finder():
    st_yr = int(input("From Year "))
    en_yr = int(input("to year "))
    list = []
    while st_yr <= en_yr:
        url = "https://en.wikipedia.org/wiki/" + str(st_yr) + "_in_film"
        web_code = requests.get(url)
        plain_text = web_code.text
        soup = BeautifulSoup(plain_text ,'html.parser')
        for movietable in soup.findAll('tr' ):
            for moviecolumn in movietable.findAll('td'):
                for moviedetails in moviecolumn.findAll('i'):
                    for namelink in moviedetails.findAll({'a':'title'}):
                        names = namelink.get('title')
                        movies = "https://en.wikipedia.org/wiki/" + names.replace(" ", "_")
                        movieslink = movies.replace("'" , "%27")
                        Movie_name = names + '  --  ' + movieslink
                        try:
                            if int(names[-10:-6]) < st_yr:
                                pass
                            else:
                                list.append(str(Movie_name))
                        except:
                            list.append(str(Movie_name))

        st_yr += 1

    max_value = len(list)
    user_input = 0
    while user_input == 0:
        random_number = random.randrange(1, max_value)
        print(list[random_number])
        user_input = int(input("For next Movie press 0 and Enter else press any other number other than 0 and press Enter :\n"))


Movies_finder()