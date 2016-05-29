from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import LoadFileForm
from . import models
from .db_logic import Database
from django.template.loader import render_to_string
from django.shortcuts import redirect
import json

mydb = Database()

def index(request):
    template = loader.get_template('lab2_app/app.html')

    return HttpResponse(template.render(None, request))


def upload_file(request):
    if request.method == 'POST':
        mydb.upload_file('data.csv')
        author = mydb.getTable("author")
        format = mydb.getTable("format")
        photoalbum = mydb.getTable("photoalbum")
        place = mydb.getTable("place")
        photos = mydb.getTable("photo")

        print("RENDER")
        print photos
        redirect('/lab2_app/')
        return render(request, 'lab2_app/app.html', {'response': {'photos': photos}})

def load_crud(request):
    if request.method == 'GET':
        print "HERE, AJAX"
        photos = mydb.getTable('photo')
        html = render_to_string('lab2_app/table.html', {'photos': photos})
        return HttpResponse(html)

def update_photo(request):
    if request.method == 'GET':
        print "update_photo " + request.GET["number"];
        print "RUNNING"
        mydb.updatePhoto(request)
        return HttpResponse("Done.")

def delete_photo(request):
    if request.method == "GET":
        mydb.deleteFromTableByID("photo", request.GET["number"])

def add_photo(request):
    if request.method == "GET":
        mydb.insertPhoto(request)
        template = loader.get_template('lab2_app/app.html')
        return redirect('/lab2_app/')

def search_photo(request):
    if request.method == "GET":
        photos = mydb.getPhoto(request)
        html = render_to_string('lab2_app/table.html', {'photos': photos})
        return HttpResponse(html)

def search_author(request):
    if request.method == "GET":
        author = mydb.getAuthor(request)
        print author
        html = render_to_string('lab2_app/author.html', {'authors': author})
        return HttpResponse(html)

def get_match_photo(request):
    if request.method == "GET":
        photos = mydb.get_match_photo(request)
        html = render_to_string('lab2_app/table.html', {'photos': photos})
        return HttpResponse(html)

def get_authors(request):
    authors = mydb.getTable("author")
    return HttpResponse(json.dumps(authors), content_type = "application/json")

def get_photoalbums(request):
    photoalbums = mydb.getTable("photoalbum")
    return HttpResponse(json.dumps(photoalbums), content_type = "application/json")

def get_places(request):
    places = mydb.getTable("place")
    return HttpResponse(json.dumps(places), content_type = "application/json")

def get_formats(request):
    formats = mydb.getTable("format")
    return HttpResponse(json.dumps(formats), content_type = "application/json")




