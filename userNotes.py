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
    print(id)
    testVar = requests.get('http://127.0.0.1:5002/getNotes')
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
    conn = sqlite3.connect("model/myDB.db")
    if subject:
        subjectList = tuple(subject.split(" "))
        print(subjectList)
        cursor = conn.execute("SELECT * FROM NOTES where SUBJECT in {subjectList}".format(subjectList=subjectList))
        dict = ({int(row[0]):row[1:] for row in cursor})
    else:
        cursor = conn.execute("SELECT * FROM NOTES")
        dict = ({int(row[0]):row[1:] for row in cursor})
    secondCursor = conn.execute("SELECT * FROM NOTES")
    # dict["subjects"] = list(set([row[1] for row in secondCursor ]))
    dict = json.dumps(dict)
    conn.close()
    return dict
# conn = sqlite3.connect('model/myDB.db')
# cursor = conn.execute("SELECT * FROM NOTES")
# for row in cursor:
#     print(row)
# conn.close()

