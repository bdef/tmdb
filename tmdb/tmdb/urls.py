from django.urls import include, path

from movies import urls


# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    # the only URLs we're using in the project are from the movies app
    path('', include('movies.urls')),
]
