from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    response=requests.get("https://dummyjson.com/recipes").json()
    tagsresponse = requests.get("https://dummyjson.com/recipes/tags").json()
    context={
        "data":response['recipes'],
        "tags":tagsresponse,
    }
    return render(request,"index.html",context)

def search(request):
    query=request.POST.get("query")
    searchresponse=requests.get(f"https://dummyjson.com/recipes/search?q={query}").json()
    tagsresponse = requests.get("https://dummyjson.com/recipes/tags").json()
    context = {
        "data": searchresponse['recipes'],
        "tags": tagsresponse,
    }
    return render(request,"index.html",context)

def receipes(request,id):
    receiperesponse=requests.get(f"https://dummyjson.com/recipes/{id}").json()
    tagsresponse = requests.get("https://dummyjson.com/recipes/tags").json()
    related_recipes = requests.get(f"https://dummyjson.com/recipes/tag/{receiperesponse['tags'][0]}").json()
    context={
        "receipe":receiperesponse,
        "tags": tagsresponse,
        "related_recipes": related_recipes['recipes'][:3],
    }
    return render(request,"receipes.html",context)

def mealtype(request,meal):
    response = requests.get(f"https://dummyjson.com/recipes/meal-type/{meal}").json()
    tagsresponse = requests.get("https://dummyjson.com/recipes/tags").json()
    context = {
        "data": response['recipes'],
        "tags": tagsresponse,
    }
    return render(request,"index.html",context)

def databytags(request,tag):
    response = requests.get(f"https://dummyjson.com/recipes/tag/{tag}").json()
    tagsresponse = requests.get("https://dummyjson.com/recipes/tags").json()
    context = {
        "data": response['recipes'],
        "tags": tagsresponse,
    }
    return render(request,"index.html",context)