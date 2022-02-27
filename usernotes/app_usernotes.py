"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response, app
from flask_restful import Api, Resource
import requests

from usernotes.notemodel import Users_notes

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_usernotes = Blueprint('app_usernotes', __name__,
                          url_prefix='/usernotes',
                          template_folder='templates/usernotes/',
                          static_folder='static',
                          static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_usernotes)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users_notes table queries"""


# Users_notes extraction from SQL
def Users_notes():
    """converts Users_notes table into JSON list """
    return [peep.read() for peep in Users_notes.query.all()]


def Users_notes_ilike(term):
    """filter Users_notes table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Users_notes.query.filter((Users_notes.name.ilike(term)) | (Users_notes.subject.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def Users_notes(userid):
    """finds User in table matching userid """
    return Users_notes.query.filter_by(userID=userid).first()


# User extraction from SQL
def Users_notes_by_subject(subject):
    """finds User in table matching subject """
    return Users_notes.query.filter_by(subject=subject).first()


""" app route section """


# Default URL
@app_usernotes.route('/viewnotes/')
def viewnotes():
    """obtains all Users_notes from table and loads Admin Form"""
    return render_template("viewnotes.html", table=Users_notes())


# CRUD create/add
@app_usernotes.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users_notes table"""
    if request.form:
        po = Users_notes(
            request.form.get("name"),
            request.form.get("subject"),
            request.form.get("notes")
        )
        po.create()
    return redirect(url_for('userntoes.viewnotes'))


# CRUD read
@app_usernotes.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users_notes table"""
    table = []
    if request.form:
        userid = request.form.get("userid")
        po = Users_notes(userid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("viewnotes.html", table=table)


# CRUD update
@app_usernotes.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users_notes table"""
    if request.form:
        userid = request.form.get("userid")
        name = request.form.get("name")
        po = Users_notes(userid)
        if po is not None:
            po.update(name)
    return redirect(url_for('crud.crud'))


# CRUD delete
@app_usernotes.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users_notes table"""
    if request.form:
        userid = request.form.get("userid")
        po = Users_notes(userid)
        if po is not None:
            po.delete()
    return redirect(url_for('crud.crud'))


# Search Form
@app_usernotes.route('/search/')
def search():
    """loads form to search Users_notes data"""
    return render_template("search.html")


# Search request and response
@app_usernotes.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(Users_notes_ilike(term)), 200)
    return response


""" API routes section """




class Users_notesAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, name, subject, notes):
            po = Users_notes(name, subject, notes)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {name}, either a format error or is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return Users_notes()

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return Users_notes_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, email, name):
            po = Users_notes_by_subject(email)
            if po is None:
                return {'message': f" is not found"}, 210
            po.update(name)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, name, subject, notes):
            po = Users_notes_by_subject(subject)
            if po is None:
                return {'message': f"{subject} is not found"}, 210
            po.update(name, subject, notes)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, userid):
            po = Users_notes(userid)
            if po is None:
                return {'message': f"{userid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:name>/<string:email>/<string:password>/<string:phone>')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:email>/<string:name>')
    api.add_resource(_UpdateAll, '/update/<string:email>/<string:name>/<string:password>/<string:phone>')
    api.add_resource(_Delete, '/delete/<int:userid>')


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://127.0.0.1:5222/crud'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/read/ilike/John', "get"],
        ['/read/ilike/com', "get"],
        ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete/4', "delete"],
        ['/delete/5', "delete"],
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Users_notes table")
    for user in Users_notes():
        print(user)


"""validating api's requires server to be running"""
if __name__ == "__main__":
    print("hello")
    api_tester()
    api_printer()