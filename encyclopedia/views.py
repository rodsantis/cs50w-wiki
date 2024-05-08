from django.shortcuts import render

# Using for testing
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request):
    return render(request, "encyclopedia/wiki.html")


def wiki_result(request, name):
    return HttpResponse(f"This will be Wiki result for {name}")