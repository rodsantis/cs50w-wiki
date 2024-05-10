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


def wiki_search(request):
    if request.method == "POST":
        entry_list = util.list_entries()
        final_list = [item.lower() for item in entry_list]
        name = request.POST
        name = name['q'].lower()
        if name in final_list:
            return render(request, "encyclopedia/search.html", {
                "name": name,
                "information": util.get_entry(name)
            })
        else:
            results = list()
            for item in final_list:
                if name in item:
                    results.append(item)
                else:
                    continue

            final_results = [item.capitalize() for item in results]
            
            return render(request, "encyclopedia/search.html", {
                "name": "Search",
                "entries": final_results
            })