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

@userNotes.route('/userNotesPage/')
def userNotesPage():
    return render_template("userNotesPage.html")

@userNotes.route('/updateNotes/',methods=["GET","POST"])
def updateNotes():
    if request.form:
        subject = (request.form.get("subject"))
        question = (request.form.get("question"))
        answer = (request.form.get("answer"))
        conn = sqlite3.connect("model/myDB.db")
        conn.execute("INSERT INTO NOTES (SUBJECT,QUESTION,ANSWER) VALUES ('{subject}','{question}','{answer}')".format(subject=subject,question=question,answer=answer))
        conn.commit()
        print("values have been added")
    return render_template("userNotesPage.html")

# conn = sqlite3.connect('model/myDB.db')
# cursor = conn.execute("SELECT * FROM NOTES")
# for row in cursor:
#     print(row)
# conn.close()