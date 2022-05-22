from django.shortcuts import render, HttpResponse, Http404
import string
import json
import MainApp.models

name = 'Морозов А.В.'
with open("Country-Langs.json", "r") as read_file:
    countries = json.load(read_file)

# countries = MainApp.models.Country_o.objects.all()


# l - словарь уникальных языков
l = {"langs": []}
for c in countries:
    for i in range(0, len(c["languages"])):
        if c["languages"][i] not in l["langs"]:
            l["langs"].append(c["languages"][i])

def home(request):
    return render(request, "index.html")


# def countries_list(request):
#     info = '<lo>'
#     for country in countries:
#         info += f'<li> <a href="\country-page\{country["Id"]}"> {country["Country"]} </a> </li>'
#     info += '</lo>'
#     return HttpResponse(info)
#
#
# def country_page(request, id):
#     for country in countries:
#         if country["Id"] == id:
#             info = f'<b>Название страны: {country["Country"]}</b>'
#     info += f'<div> <a href="\countries-list"> Назад </a> <div>'
#     return HttpResponse(info)


# def about(request):
#     context = {
#         "name": "Александр"
#     }
#     return render(request, "about.html", context)


def items(request, alf):
    content = countries.copy()
    for cn in countries:
        if (alf != "No") and (cn["country"][0] != alf):
            content.remove(cn)
    d = {"country": content}
    return render(request, "items.html", d)


def item_page(request, it):
    for c in countries:
        if c["country"] == it:
            return render(request, "item-page.html", c)
    raise Http404("Не найден !")


def langs(request, alf):
    ll = l.copy()
    for cn in l["langs"]:
        if (alf != "No") and (cn[0] != alf):
            ll["langs"].remove(cn)
    return render(request, "langs.html", ll)


def l2c(request, it):
    content = countries.copy()
    for cn in countries:
        if  ( it not in cn["languages"]):
            content.remove(cn)
    d = {"country": content, "lang": it}
    return render(request, "l2c.html", d)
