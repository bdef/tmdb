from datetime import datetime

from django.db import models


class Movie:
    '''
    note that we're not inheriting from Django's Model.
    that's because nothing lives in the DB (as of yet).
    but it's still convenient to have a class!
    i'm putting this class here, because though it isn't a Django Model,
    it's a model in the MVT/MVC sense.
    '''
    # python dt formats: https://docs.python.org/3/library/datetime.html
    json_date_fmt = '%Y-%m-%d'

    def __init__(self, json):
        self.tmdb_id = json['id']
        self.title = json['title']
        self.popularity = json['popularity']
        self.poster_path = json['poster_path']
        self.overview = json['overview']
        try:
            self.release_date = datetime.strptime(json['release_date'], self.json_date_fmt).date()
        except ValueError:
            # some items in the feed have an empty str for release date!
            self.release_date = False

    def poster_src(self):
        return "https://image.tmdb.org/t/p/w185_and_h278_bestv2{}".format(self.poster_path)

    def poster_src_big(self):
        return "https://image.tmdb.org/t/p/w370_and_h556_bestv2{}".format(self.poster_path)
    
    def release_year(self):
        try:
            return self.release_date.year
        except:
            return 'tbd'