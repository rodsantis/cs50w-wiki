from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="wiki_index"),
    path("wiki/<str:name>", views.wiki, name="wiki"),
    path("", views.errorpage, name="error"),
    path("wiki/search/", views.wiki_search, name="search"),
    path("new-entry/", views.new_entry, name="new-entry"),
]
