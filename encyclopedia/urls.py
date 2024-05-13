from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="wiki_index"),
    path("wiki/<str:name>", views.wiki, name="wiki"),
    path("", views.errorpage, name="error"),
    path("", views.error_exists, name="error-exists"),
    path("wiki/search/", views.wiki_search, name="search"),
    path("new-entry/", views.new_entry, name="new-entry"),
    path("edit/<str:name>", views.edit_page, name="edit"),
    path("wiki/random/", views.random_page, name="random-page")
]
