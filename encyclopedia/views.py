from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util

# Using for testing
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, name):
    if util.get_entry(name) == None:
        return errorpage(request, name, 404)
    return render(request, "encyclopedia/wiki.html", {
        "name": name.capitalize(),
        "information": util.get_entry(name),
    })


def errorpage(request, name, number):
    return render(request, "encyclopedia/error.html", {
        "number": number,
        "name": name,
    })