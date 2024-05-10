from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
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


def wiki_search(request, name):
    ...
    # if request.method == "POST":
    #     name = request.POST
    #     name = name['q']
    #     return HttpResponseRedirect(reverse("wiki", args=(q.id,)))
    #     entry_list = util.list_entries()
    #     if name in entry_list:
    #         return render(request, "encyclopedia/wiki/<str:name>.html", {
    #             "name": name,
    #             "information": util.get_entry(name),
    #         })
    #     if name not in entry_list:
    #         list_result = []
    #         for item in entry_list:
    #             if name in item:
    #                 list_result.append(item)
    #             continue
    #         return render(request, "encyclopedia/wiki.html", {
    #             "name": "Wiki",
    #             "entries": list_result
    #         })