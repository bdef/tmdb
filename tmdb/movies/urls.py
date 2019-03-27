from django.urls import path

from . import views

urlpatterns = [
    # a request for the site root will be served the index view
    path('', views.index, name='index'),
    # a request for a particular movie will be served the detail view,
    # django sends the id number of that movie to the view. thanks, django!
    path('<int:tmdb_id>/', views.detail, name='detail'),
]