from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import util


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={"style": "height:300px; width:600px"}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, name):
    if request.method == "POST":
        name = name
        change = request.POST
        change = change['edit-entry']
        util.save_entry(name, change)
        return render(request, "encyclopedia/wiki.html", {
            "name": name.capitalize(),
            "information": util.get_entry(name),
        })
    if util.get_entry(name) == None:
        return errorpage(request, name, 404)
    return render(request, "encyclopedia/wiki.html", {
        "name": name.capitalize(),
        "information": util.get_entry(name),
    })


def errorpage(request, name, number):
    return render(request, "encyclopedia/404.html", {
        "number": number,
        "name": name,
    })


def error_exists(request, name, number):
    return render(request, "encyclopedia/409.html", {
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
                "name": name.capitalize(),
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


def new_entry(request):
    if request.method == "POST":
        entry_list = util.list_entries()
        final_list = [item.lower() for item in entry_list]
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if title.lower() in final_list:
                return error_exists(request, title, 409)
            description = form.cleaned_data["description"]
            util.save_entry(title, description)
            return render(request, "encyclopedia/wiki.html", {
                "name": title.capitalize(),
                "information": util.get_entry(title),
            })
        else:
            return render(request, "encyclopedia/newentry.html", {
                "form": form
            })


    return render(request, "encyclopedia/newentry.html", {
        "form": NewEntryForm()
    })


def edit_page(request, name):
    if request.method == "POST":
        name = name
        return render(request, "encyclopedia/editpage.html", {
            "name": name,
            "information": util.get_entry(name)
        })