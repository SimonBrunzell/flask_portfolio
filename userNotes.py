import sqlite3
from flask import Flask, render_template,request,Blueprint
import requests
import json
import random
from subjects import subjects
import math
import pandas as pd
from aboutus import aboutus
from sanjay_createTask import recommendation
from __init__ import app

userNotes = Blueprint("userNotes",__name__)

@userNotes.route('/userNotesPage/',methods=["GET","POST"])
def userNotesPage():
    id=0
    params=''
    if request.form:
        id = request.form.get("my_id")
        if id=="adding":
            subject = (request.form.get("subject"))
            question = (request.form.get("question"))
            answer = (request.form.get("answer"))
            conn = sqlite3.connect("model/myDB.db")
            conn.execute("INSERT INTO NOTES (SUBJECT,QUESTION,ANSWER) VALUES ('{subject}','{question}','{answer}')".format(subject=subject,question=question,answer=answer))
            conn.commit()
            conn.close()
            print("values have been added")
        if id=="deleting":
            toDelete = request.form.get("id")
            conn = sqlite3.connect("model/myDB.db")
            conn.execute("DELETE FROM NOTES WHERE id={id}".format(id=toDelete))
            conn.commit()
            conn.close()
        if id=="searching":
            term = request.form.get("searchTerm")
            params +="?search="
            params+= term
    print(id)
    testVar = requests.get('http://127.0.0.1:5002/getNotes'+params)
    output = testVar.json()
    return render_template("userNotesPage.html",data=output)

@userNotes.route("/sortUserNotes/",methods=["GET","POST"])
def sortUserNotes():
    params = '?subject='
    if request.form:
        id = request.form.get("my_id")
        subjects = (request.form.getlist("subjects"))
        print("the user has selected "+str(subjects))
        for subject in subjects:
            params += ("{}+".format(subject))
    print("STUFF IS BEING PRINTED")
    testVar = requests.get('http://127.0.0.1:5002/getNotes'+params)
    output = testVar.json()
    return render_template("userNotesPage.html",data=output)


@app.route("/getNotes/")
def getNotes():
    subject=request.args.get("subject")
    search = request.args.get("search")
    conn = sqlite3.connect("model/myDB.db")
    print(search)
    if search:
        firstCursor = conn.execute("SELECT * FROM NOTES WHERE subject LIKE '%{term}%'".format(term=search))
        secondCursor = conn.execute("SELECT * FROM NOTES WHERE question LIKE '%{term}%'".format(term=search))
        thirdCursor = conn.execute("SELECT * FROM NOTES WHERE answer LIKE '%{term}%'".format(term=search))
        dict = {}
        for row in firstCursor:
            dict[row[0]] = row[1:]
            print(row)
        for row in secondCursor:
            dict[row[0]] = row[1:]
            print(row)
        for row in thirdCursor:
            dict[row[0]] = row[1:]
            print(row)
    else:
        cursor = conn.execute("SELECT * FROM NOTES")
        dict = ({int(row[0]):row[1:] for row in cursor})
    # secondCursor = conn.execute("SELECT * FROM NOTES")
    # dict["subjects"] = list(set([row[1] for row in secondCursor ]))
    dict = json.dumps(dict)
    conn.close()
    return dict
# conn = sqlite3.connect('model/myDB.db')
# cursor = conn.execute("SELECT * FROM NOTES where answer LIKE '%George%'")
# for row in cursor:
#     print(row)
# conn.close()

