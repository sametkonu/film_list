import pandas as pd
from getInfo import getMovieInfo

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

getInfo = getMovieInfo()
df = getInfo.movieInfo()
print(df)






"""

########################################################################################################################


def get_user_choice():
    print("\n[1] Filter movies by 1 field")
    print("[2] Filter movies by 2 fields")
    print("[q] Quit.")
    return input("What would you like to do? ")


def get_filtering_choice():
    print("\n[1] Genre")
    print("[2] Movie Length")
    print("[3] Actor")
    print("[4] Director")
    print("[q] Quit.")
    return input("Please choose a filtering field? ")


def filtering_by_genre(df):
    print("\nFiltering movies by Genre:\n")
    print("Some Acceptable Genres: Drama/Crime/Action/Biography/Adventure/Western/Romance/Sci-Fi/"
          "\nFantasy/Mystery/Comedy/Thriller/Family/War/Animation/Music/Horror/History/Musical/Sport\n")

    input_genre = input("Please enter a proper genre: ")
    filtered_data = df[df['genre'].str.contains(input_genre)]
    print(filtered_data[['ranking','movieTitle', 'movieYear', 'rating', 'movieLength', 'genre', 'country', 'language',
                         'production']])


def filtering_by_runtime(df):
    print("\nFiltering movies by runtime\n")
    input_runtime = input("Please enter the movie length in minutes: ")
    answer = input("Would you like movies OVER: " + input_runtime + " minutes? y/n: ")
    if answer == 'y':
        print("Looking for movies OVER " + input_runtime + " minutes...")
        filtered_data = df[pd.to_numeric(df['runtime']) >= int(input_runtime)]
        print(filtered_data[['ranking','movieTitle', 'movieYear', 'rating', 'movieLength', 'genre', 'country',
                             'language', 'production']])
    elif answer == 'n':
        print("Looking for movies UNDER " + input_runtime + " minutes...")
        filtered_data = df[pd.to_numeric(df['runtime']) <= int(input_runtime)]
        print(filtered_data[['ranking','movieTitle', 'movieYear', 'rating', 'movieLength', 'genre', 'country',
                             'language', 'production']])
    else:
        print("\nPlease enter a valid option.\n")


def filtering_by_actor(df):
    print("\nFiltering movies by Actor:\n")
    input_actor = input("Please enter actor's fullname: ")
    filtered_data = df[df['starList'].str.contains(input_actor)]
    print(filtered_data[['ranking','movieTitle', 'movieYear', 'rating', 'movieLength', 'genre', 'country', 'language',
                         'production']])


def filtering_by_director(df):
    print("\nFiltering movies by Director:\n")
    input_director = input("Please enter Director's fullname: ")
    filtered_data = df[df['director'].str.contains(input_director)]
    print(filtered_data[['ranking','movieTitle', 'movieYear', 'rating', 'movieLength', 'genre', 'country', 'language',
                         'production']])


def filtering_by_2fields(df):
    print("\nFiltering movies by 2 fields:")
    print("\nFiltering movies by Runtime and Genre fields:\n")
    print("Some Acceptable Genres: Drama/Crime/Action/Biography/Adventure/Western/Romance/Sci-Fi/"
          "\nFantasy/Mystery/Comedy/Thriller/Family/War/Animation/Music/Horror/History/Musical/Sport\n")

    input_genre = input("Please enter a proper genre: ")
    input_runtime = input("Please enter the movie length in minutes: ")
    answer = input("Would you like movies OVER: " + input_runtime + " minutes? y/n: ")
    if answer == 'y':
        print("Looking for movies with genre = " + input_genre + " and OVER " + input_runtime + " minutes...")
        runtime_filter = pd.to_numeric(df['runtime']) >= int(input_runtime)
        genre_filter = df['genre'].str.contains(input_genre)
        all_filter = runtime_filter & genre_filter
        print(df[all_filter][['ranking','movieTitle', 'movieYear', 'rating', 'movieLength', 'genre', 'country',
                              'language', 'production']])
    elif answer == 'n':
        print("Looking for movies with genre = " + input_genre + " and UNDER " + input_runtime + " minutes...")
        runtime_filter = pd.to_numeric(df['runtime']) <= int(input_runtime)
        genre_filter = df['genre'].str.contains(input_genre)
        all_filter = runtime_filter & genre_filter
        print(df[all_filter][['ranking','movieTitle', 'movieYear', 'rating', 'movieLength', 'genre', 'country',
                              'language', 'production']])
    else:
        print("\nPlease enter a valid option.\n")


def filtering_by_1field(df):
    print("\nFiltering movies by 1 field:\n")
    filtering_choice = ''
    while filtering_choice != 'q':
        filtering_choice = get_filtering_choice()
        if filtering_choice == '1':
            filtering_by_genre(df)
        elif filtering_choice == '2':
            filtering_by_runtime(df)
        elif filtering_choice == '3':
            filtering_by_actor(df)
        elif filtering_choice == '4':
            filtering_by_director(df)
        elif filtering_choice == 'q':
            print("\nReturning to main menu.")
        else:
            print("\nI didn't understand that choice.\n")


#######################################################################################################################
choice = ''
display_title_bar()

if os.path.isfile("IMDBTop250.csv"):
    print("\nReading from csv file..")
    imdb = pd.read_csv("IMDBTop250.csv")
else:
    print("\nDownloading IMDB Top 250 movies into a CSV file..")
    imdb = download_imdb_top250()

while choice != 'q':
    choice = get_user_choice()
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        filtering_by_1field(imdb)
    elif choice == '2':
        filtering_by_2fields(imdb)
    elif choice == 'q':
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")

"""
