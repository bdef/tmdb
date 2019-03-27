from urllib.parse import quote_plus

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests

from .models import Movie


def index(request):
    # view for the project's home page
    query = request.GET.get('query', '')
    if query:
        # user is searching, hit TMDB's search
        api_url = "{url}search/movie?query={q}&api_key={key}".format(
            url=settings.TMDB_API_BASE_URL,
            q=quote_plus(query),
            key=settings.TMDB_API_KEY)
    else:
        # user isn't searching; get the movies sorted by popularity
        api_url = '{url}discover/movie?sort_by=popularity.desc&api_key={key}'.format(
            url=settings.TMDB_API_BASE_URL,
            key=settings.TMDB_API_KEY)
    # page keeps track of _where_ we are in the results
    page = int(request.GET.get('page', 1))
    page_url = "{url}&page={page}".format(url=api_url, page=page)
    # requests is a great lib that makes a lot of things easier:
    # http://docs.python-requests.org/en/master/
    # time to hit TMDB's API!
    r = requests.get(page_url)
    if r.status_code == 200:
        # success! let's process the results
        json = r.json()
        # a list of movies to display
        movies = []
        for movie_json in json['results']:
            movies.append(Movie(movie_json))
        # do we want Previous/Next page buttons on results?
        # while the response DOES include a total_pages value, this doesn't work at pages > 1000,
        # per TMDB's API: https://www.themoviedb.org/documentation/api/status-codes
        if json['total_pages'] > 1 and page < 1000 :
            next_page = page + 1
        else:
            next_page = False
        if page-1 > 0:
            prev_page = page - 1
        else:
            prev_page = False
        # context=variables we want accessible from the template, via django magic
        context = {
            'movies': movies,
            'next_page': next_page,
            'prev_page': prev_page,
            'query': query}
        return render(request, 'movies/index.html', context)
    else:
        # the request failed? out of laziness we'll just return a response
        # w/ the same status code we got from our request TMDB's API
        return HttpResponse('SOMETHING BAD HAPPENED!', status=r.status_code)


def detail(request, tmdb_id):
    # view for details of a movie. tmdb_id is an arg provided by django magic,
    # via the path defined in urls.py
    # build the api url we're gonna hit
    url = "{url}movie/{id}?api_key={key}".format(
        url=settings.TMDB_API_BASE_URL,
        id=tmdb_id,
        key=settings.TMDB_API_KEY)
    # now GET it!
    r = requests.get(url)
    if r.status_code == 200:
        context = {
            # grab the movie json from the response & build a Movie obj with it
            'movie': Movie(r.json()),
        }
        return render(request, 'movies/detail.html', context)
    else:
        return HttpResponse('SOMETHING BAD HAPPENED!', status=r.status_code)
