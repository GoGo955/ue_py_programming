"""
Module used for reading movie data from csv's.
"""
import csv
import glob


class ReadData():
    """
    Class used for simplify reading the data.
    """
    def __init__(self, row, header) -> None:
        self.__dict__ = dict(zip(header, row))


csv_files = glob.glob("data/*.csv")

# list of lists with data
data = [list(csv.reader(open(file_name, encoding="utf8"))) for file_name in csv_files]

# ['links.csv', 'movies.csv', 'tags.csv']
LINKS = [ReadData(i, data[0][0]).__dict__ for i in data[0][1:]]
MOVIES = [ReadData(i, data[1][0]).__dict__ for i in data[1][1:]]
RATINGS = [ReadData(i, data[2][0]).__dict__ for i in data[2][1:]]
TAGS = [ReadData(i, data[3][0]).__dict__ for i in data[3][1:]]
