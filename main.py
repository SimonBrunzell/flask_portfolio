# import "packages" from flask
from flask import Flask, render_template,request
import requests
import json
import random
#from crud.app_crud import app_crud

from subjects import subjects
import math
import pandas as pd
from aboutus import aboutus
from userNotes import userNotes


# create a Flask instance
from __init__ import app

#app.register_blueprint(app_crud)

app.register_blueprint(subjects)

app.register_blueprint(aboutus)

app.register_blueprint(userNotes)
# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/leahcreate/')
def leahcreate():
    return render_template("leahcreate.html")

@app.route('/viewnotes/')
def viewnotes():
    return render_template("viewnotes.html")

@app.route('/snake/')
def snake():
    return render_template("snake.html")

@app.route('/darktest/')
def darktest():
    return render_template("about_us/darktest.html")

@app.route('/memorygame/')
def memorygame():
    return render_template("memorygame.html")

@app.route("/final_grade_calc/")
def final_grade_calc():
    return render_template("final_grade_calc.html")
@app.route('/apec/')
def apec():
    return render_template("subjects/apec.html")

@app.route('/apush/')
def apush():
    return render_template("subjects/apush.html")

@app.route('/biology/')
def biology():
    return render_template("subjects/biology.html")

@app.route('/calcab/')
def calcab():
    return render_template("subjects/calcab.html")

@app.route('/chemistry/')
def chemisty():
    return render_template("subjects/chemistry.html")

@app.route('/csp/')
def csp():
    return render_template("subjects/csp.html")

@app.route('/stats/')
def stats():
    return render_template("subjects/stats.html")

@app.route('/notes/')
def notes():
    return render_template("subjects/notes.html")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/planner/')
def planner():
    return render_template('weekly calendar.html')

# runs the application on the development server
@app.route('/flashcards/')
def flashcards():
    testVar = requests.get('http://127.0.0.1:5002/getNotes')
    output = testVar.json()
    return render_template('flashcards.html',data=output)

@app.route('/compscitools/')
def compscitools():
    return render_template('compscitools.html')

@app.route('/rateThis/', methods=['GET', 'POST'])
def rateThis():
    return render_template("rateThis.html")

@app.route('/studycycle/', methods=['GET', 'POST'])
def studycycle():
    return render_template("studycycle.html")

@app.route('/binary_calc/',methods=['GET', 'POST'])
def binary_calc():
    output = [x+1 for x in range(10)]
    if request.form:
        length = request.form.get("length")
        target = request.form.get('target')
        if len(str(length)) != 0:
            output = sorted(random.sample(range(0,500),int(length)))
        if len(str(target)) == 0:
            target = 2
    target = int(target)
    result = {}
    low = 0
    high = len(output)-1
    search = 1
    found = False
    while low<=high:

        mid = int((low+high)/2)
        result["search"+str(search)] = {"mid":mid,"low":low,"high":high}
        if output[mid] == target:
            found = True
            break
        elif output[mid]<target:
            low = mid+1
        else:
            high = mid-1
        search += 1
    result["finalsearch"] = found
    print(result)
    return render_template("compscitools.html",output =output, jsOutput = json.dumps(result), target = target)
@app.route('/courserecoms/')
def courserecoms():
    return render_template('courserecoms.html')
@app.route('/challenges/')
def challenges():
    return render_template('challenges.html')
@app.route("/challenges_calc/",methods=['GET', 'POST'])
def challenges_calc():
    number = 3
    if request.form:
        print("ad")
        number = int(request.form.get("num"))
        if number % 2 == 0:
            even = "Even"
        else:
            even = "Odd"
        prime = True
        for x in range(2,number):
            if number % x ==0:
                prime = False
                break
                                                                     
    return render_template("challenges.html",number = number, even = even, prime=prime)

# @app.route("/sanjay_createTask/", methods=["GET","POST"])
# def sanjay_createTask():
#     genres = []
#     if request.form:
#         genres = request.form.getlist("genre")
#     output = recommendation(genres)
#     print(output)
#     data = pd.read_csv("movieData/movies.csv")
#     return render_template("sanjay_createTask.html",output=output,movies = json.dumps(data["title"].to_list()))

@app.route("/mcq/")
def mcq():
    response = requests.get("https://api.trivia.willfry.co.uk/questions?limit=10")
    output = response.json()
    for x in range(len(output)):
        print(output[x])
    return render_template("mcq.html",questions = output)
if __name__ == "__main__":
    app.run(debug=True, port="5002")
