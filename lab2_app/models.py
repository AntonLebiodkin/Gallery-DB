from __future__ import unicode_literals

from django.db import connection






class Author():
    def __init__(self, name, surname, author, format, photoalbum, place):
        self.name = name
        self.surname = surname
        self.author = author
        self.format = format
        self.photoalbum = photoalbum
        self.place = place




class Format():
    def __init__(self, format):
        self.format = format


class Photoalbum():
    def __init__(self, name):
        self.name = name


class Place():
    def __init__(self, country, city):
        self.country = country
        self.city = city

class Photo():
    def __init__(self, name, author, format, photoalbum, place):
        self.name = name
        self.author = author
        self.format = format
        self.photoalbum = photoalbum
        self.place = place


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def getPhoto():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM photo")
    print dictfetchall(cursor)