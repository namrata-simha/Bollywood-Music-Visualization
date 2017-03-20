import urllib.request
import urllib
import re
import csv
import numpy as np
from itertools import islice

categories = []

def getItem(item):
    song = item.split("<span itemprop=\"name\">", 1)[1]
    item = re.split("<", song)[0]
    item = removeCommas(item)
    return item, song

def getSinger(singer):
    singer, song = getItem(singer)
    comma = re.split("</span>", song)[1]
    comma = re.split("<",comma)[0]
    if comma == ",":
        singerNext, song = getSinger(song)
        singer = singer + "*" + singerNext
    # singer = removeCommas(singer)
    return singer, song

def getActors(actor):
    song = actor.split(">", 1)[1]
    actor = re.split("<", song)[0]
    comma = re.match(".*,", actor)
    if comma:
        song = song.split("href=\"/actor", 1)[1]
        actorNext, song = getActors(song)
        actor = actor + actorNext
    return actor, song

def removeCommas(data):
    return data.replace(",", "")

def populateDataset():
    for pageNo in range(1, 4):
        url = 'http://www.hindigeetmala.net/category/index.php?page='+str(pageNo)
        try:
            page = urllib.request.urlopen(url)
        except:
            # print("Wikipedia page not found")
            print("Not_found")
        dataStr = str(page.read())
        dataStr = dataStr.split("Top Category on HindiGeetMala as per number of songs available at our site")
        dataStr = dataStr[1].split("href=\"/disclaimer")[0]
        dataStr = dataStr.split("href=\"")
        for i in range(1, len(dataStr)):
            dataStr[i] = dataStr[i].split("\"")[0]
            if i%2 == 0:
                categories.append(dataStr[i])
    # print(*categories, sep='\n')

    genres = []
    songNames = []
    singers = []
    musicDirectors = []
    lyricists = []
    movies = []
    years = []
    actors = []
    youtubeLinks = []

    genres.append("genre")
    songNames.append("songName")
    singers.append("singer")
    musicDirectors.append("musicDirector")
    lyricists.append("lyricist")
    movies.append("movie")
    years.append("year")
    actors.append("actors")
    youtubeLinks.append("youtubeLinks")

    for categoryNo in range(0, len(categories)):
        url = 'http://www.hindigeetmala.net' + categories[categoryNo]
        # url = 'http://www.hindigeetmala.net' + categories[0]
        try:
            page = urllib.request.urlopen(url)
        except:
            print("Not_found")
            continue
        data = str(page.read())
        # print(data)
        pages = -1
        pagesStr = data.split("Page 1 of ")[1]
        pages = int(pagesStr.split("<")[0])
        print(pages)

        for pageNo in range(1, pages+1):
            url = 'http://www.hindigeetmala.net' + categories[categoryNo] + "?page=" + str(pageNo)
            # url = 'http://www.hindigeetmala.net' + categories[0] + "?page=" + str(1)
            try:
                page = urllib.request.urlopen(url)
            except:
                print("Not_found")
            dataStr = str(page.read())
            # print(dataStr)
            try:
                dataStr = dataStr.split("Song Heading")[2]
            except:
                continue
            print(dataStr)
            songsStrs = (re.split("href=\"/song", dataStr))
            for x in range (1, len(songsStrs)):
                print("Page number: "+str(pageNo))
                genre = re.split("/category/", categories[categoryNo])[1]
                genre = re.split("\.php", genre)[0]
                genre = genre.replace("_", " ")
                genre = genre.title()
                print(genre)
                genres.append(genre)

                song = re.split("<span itemprop=\"name\"> ", songsStrs[x])[1]
                songName = re.split(" <", song)[0]
                songName = removeCommas(songName)
                print(songName)
                songNames.append(songName)

                try:
                    singer = songsStrs[x].split("href=\"/singer", 1)[1]
                    singer, song = getSinger(singer)
                except:
                    singer = "NotFound"
                print(singer)
                singers.append(singer)

                try:
                    musicDirector = songsStrs[x].split("href=\"/music_director", 1)[1]
                    musicDirector, song = getItem(musicDirector)
                except:
                    musicDirector = "NotFound"
                print(musicDirector)
                musicDirectors.append(musicDirector)

                try:
                    lyricist = songsStrs[x].split("href=\"/lyricist", 1)[1]
                    lyricist, song = getItem(lyricist)
                except:
                    lyricist = "NotFound"
                print(lyricist)
                lyricists.append(lyricist)

                try:
                    movie = songsStrs[x].split("href=\"/movie", 1)[1]
                    try:
                        year = re.split("</span> \(", movie)[1]
                        year = int(re.split("\)<", year)[0])
                    except:
                        year = 0
                    movie, song = getItem(movie)
                except:
                    movie = "NotFound"
                print(movie)
                print(year)
                movies.append(movie)
                years.append(year)

                try:
                    actor = songsStrs[x].split("href=\"/actor", 1)[1]
                    actor, song = getActors(actor)
                except:
                    actor = "NotFound"
                # print(actor)
                # actors.append(actor)

                try:
                    youtube = songsStrs[x].split("src=\"", 1)[1]
                    # song = youtube.split("<span itemprop=\"name\">", 1)[1]
                    youtube = re.split("\"", youtube)[0]
                    # youtube, song = getItem(youtube)
                except:
                    youtube = "NotFound"
                print(youtube)
                youtubeLinks.append(youtube)

                print("************************")

    finalSongsList = zip(genres, songNames, singers, musicDirectors, lyricists, movies, years, youtubeLinks)
    with open('songs.csv', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(finalSongsList)

def sortEntriesBy(item):
    genres = []
    songNames = []
    singers = []
    musicDirectors = []
    lyricists = []
    movies = []
    years = []
    actors = []
    with open("songs.csv", "r") as file:
        reader = csv.reader(file)
        for row in islice(reader, 1, None):
            genres.append(row[0])
            songNames.append(row[1])
            singers.append(row[2])
            musicDirectors.append(row[3])
            lyricists.append(row[4])
            movies.append(row[5])
            years.append(int(row[6]))
            # actors.append(row[7])

    genres = np.array(genres)
    songNames = np.array(songNames)
    singers = np.array(singers)
    musicDirectors = np.array(musicDirectors)
    lyricists = np.array(lyricists)
    movies = np.array(movies)
    years = np.array(years)
    actors = np.array(actors)

    if item == "genres":
        item = genres
    else:
        if item == "songNames":
            item = songNames
        else:
            if item == "singers":
                item = singers
            else:
                if item == "musicDirectors":
                    item = musicDirectors
                else:
                    if item == "lyricists":
                        item = lyricists
                    else:
                        if item == "movies":
                            item = movies
                        else:
                            if item == "years":
                                item = years
                            else:
                                if item == "actors":
                                    item = actors

    idx = np.argsort(item)

    genres = np.array(genres)[idx]
    songNames = np.array(songNames)[idx]
    singers = np.array(singers)[idx]
    musicDirectors = np.array(musicDirectors)[idx]
    lyricists = np.array(lyricists)[idx]
    movies = np.array(movies)[idx]
    years = np.array(years)[idx]
    # actors = np.array(actors)[idx]
    youtubeLinks = np.array(youtubeLinks)[idx]

    printList = zip(genres, songNames, singers, musicDirectors, lyricists, movies, years, youtubeLinks)
    # print(*list(printList), sep = '\n')

    uniqueItems, itemCounts = np.unique(item, return_counts=True)
    print(*list(zip(uniqueItems, itemCounts)), sep='\n')

genres = []
songNames = []
singers = []
musicDirectors = []
lyricists = []
movies = []
years = []
actors = []
youtubeLinks = []
populateDataset()
# sortEntriesBy("genres")
# print("************************")
# sortEntriesBy("songNames")
# print("************************")
# sortEntriesBy("singers")
# print("************************")
# sortEntriesBy("musicDirectors")
# print("************************")
# sortEntriesBy("lyricists")
# print("************************")
# sortEntriesBy("movies")
# print("************************")
# sortEntriesBy("years")
# print("************************")
# sortEntriesBy("actors")