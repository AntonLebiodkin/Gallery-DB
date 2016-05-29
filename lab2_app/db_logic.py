import MySQLdb as mdb
import sys
import csv


class Database:
    def __init__(self):
        self.con = mdb.connect('localhost', 'root', '1111', 'gallery')

    def upload_file(self, filename):

        with self.con:
            cur = self.con.cursor()
            cur.execute("DELETE FROM photo")
            cur.execute("DELETE FROM author")
            cur.execute("DELETE FROM format")
            cur.execute("DELETE FROM photoalbum")
            cur.execute("DELETE FROM place")
        path = 'lab2_app/static/csv/' + filename
        with open(path) as f:
            reader = f.readlines()
            for line in reader:
                params = line.split(",")
                table = params[0]
                if table == "author":
                    cur.execute("INSERT INTO author (id, name, surname, sex, age)  VALUES ('" + params[1] +"','" + params[2] + "','" + params[3] + "','" + params[4] + "','" + params[5] + "')")
                elif table == "format":
                    cur.execute("INSERT INTO format (id, format_name)  VALUES ('" + params[1] +"','" + params[2] + "')")
                elif table == "photo":
                    cur.execute("INSERT INTO photo (id, name, place_id, photoalbum_id, author_id, format_id, price)  VALUES ('" + params[1] +"','" + params[2] + "','" + params[3] + "','" + params[4] + "','" + params[5] +"','" + params[6] + "','"+ params[7]+"')")
                elif table == "place":
                    cur.execute("INSERT INTO place (id, contry, city)  VALUES ('" + params[1] +"','" + params[2] + "','" + params[3] + "')")
                elif table == "photoalbum":
                    cur.execute("INSERT INTO photoalbum (id, name)  VALUES ('" + params[1] +"','" + params[2] + "')")



    def getTable(self, name):
        if name == "photo":
            with self.con:
                cur = self.con.cursor()
                cur.execute("""SELECT photo.id, photo.name, place.city, photoalbum.name, author.surname, format.format_name, photo.price\
                               FROM photo\
                               INNER JOIN place\
                               ON photo.place_id = place.id\
                               INNER JOIN photoalbum\
                               ON photo.photoalbum_id = photoalbum.id\
                               INNER JOIN author\
                               ON photo.author_id = author.id\
                               INNER JOIN format\
                               on photo.format_id = format.id\
                            """)
                return cur.fetchall()
        else:
            with self.con:
                cur = self.con.cursor()
                cur.execute("SELECT * FROM " + name)
                return cur.fetchall()

    def deleteFromTableByID(self, table, id):
            with self.con:
                cur = self.con.cursor()
                cur.execute("DELETE FROM " + table +  " WHERE id = " + id)
                return cur.fetchall()

    def updatePhoto(self, request):
        with self.con:
            print request
            id = request.GET["number"]
            name = request.GET["name"]
            place = request.GET["place"]
            photoalbum = request.GET["photoalbum"]
            author = request.GET["author"]
            format = request.GET["format"]

            print id, name,place, photoalbum, author, format


            cur = self.con.cursor();
            cur.execute("UPDATE photo SET name = '{0}', place_id={1}, photoalbum_id={2}, author_id={3}, format_id={4}  WHERE id = {5}".format(name, place, photoalbum, author, format, id));

    def insertPhoto(self, request):
        with self.con:
            cur = self.con.cursor()
            cur.execute('INSERT INTO photo (name, place_id, photoalbum_id, author_id, format_id, price) VALUES ("{0}",{1},{2},{3},{4}, {5})'.\
            format(request.GET['name'], request.GET['place'],request.GET['photoalbum'],request.GET['author'],request.GET['format'], request.GET['price']))

    def getPhoto(self, req):
        with self.con:
            cur = self.con.cursor()
            from_price =  req.GET["from_price"]
            to_price = req.GET["to_price"]
            print from_price, to_price
            cur.execute("""SELECT photo.id, photo.name, place.city, photoalbum.name, author.surname, format.format_name, photo.price\
                               FROM photo\
                               INNER JOIN place\
                               ON photo.place_id = place.id\
                               INNER JOIN photoalbum\
                               ON photo.photoalbum_id = photoalbum.id\
                               INNER JOIN author\
                               ON photo.author_id = author.id\
                               INNER JOIN format\
                               on photo.format_id = format.id\
                               WHERE (photo.price >= {0} AND photo.price <= {1})\
                            """.format(from_price, to_price))
            return cur.fetchall()

    def getAuthor(self, req):
        with self.con:
            sex = req.GET["gender"]
            print sex
            cur = self.con.cursor()
            cur.execute("SELECT * FROM author WHERE sex={0}".format(sex))
            return cur.fetchall()

    def get_match_photo(self, req):
        with self.con:
            name = req.GET["name"]
            print name + " BACKEND FULLTEXT"
            cur = self.con.cursor()
            cur.execute("""SELECT photo.id, photo.name, place.city, photoalbum.name, author.surname, format.format_name, photo.price\
                               FROM photo\
                               INNER JOIN place\
                               ON photo.place_id = place.id\
                               INNER JOIN photoalbum\
                               ON photo.photoalbum_id = photoalbum.id\
                               INNER JOIN author\
                               ON photo.author_id = author.id\
                               INNER JOIN format\
                               on photo.format_id = format.id\
                               WHERE MATCH(photo.name, photoalbum.name) AGAINST('{0}' IN BOOLEAN MODE)\
                            """.format(name))
            return cur.fetchall()

    def getNotMatchPhoto(self, req):
        with self.con:
            name = req.GET["name"]
            print name + " BACKEND FULLTEXT"
            cur = self.con.cursor()
            cur.execute("""SELECT photo.id, photo.name, place.city, photoalbum.name, author.surname, format.format_name, photo.price\
                               FROM photo\
                               INNER JOIN place\
                               ON photo.place_id = place.id\
                               INNER JOIN photoalbum\
                               ON photo.photoalbum_id = photoalbum_id\
                               INNER JOIN author\
                               ON photo.author_id = author.id\
                               INNER JOIN format\
                               on photo.format_id = format.id\
                               WHERE MATCH(photo.name, photoalbum.name) AGAINST('{0}' IN BOOLEAN MODE)\
                            """.format(name))
            return cur.fetchall()
