# import "packages" from flask
from flask import Flask, render_template,request
import requests
import json
import random
from crud.app_crud import app_crud

from subjects import subjects
import math

from aboutus import aboutus


# create a Flask instance
from __init__ import app

app.register_blueprint(app_crud)

app.register_blueprint(subjects)

app.register_blueprint(aboutus)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/darktest/')
def darktest():
    return render_template("about_us/darktest.html")

@app.route("/final_grade_calc/")
def final_grade_calc():
    return render_template("final_grade_calc.html")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# runs the application on the development server
@app.route('/flashcards/')
def flashcards():
    return render_template('flashcards.html')

@app.route('/compscitools/')
def compscitools():
    return render_template('compscitools.html')

@app.route('/rateThis/', methods=['GET', 'POST'])
def rateThis():

    rating1 = request.form.get("rating1")
    rating2 = request.form.get('rating2')
    rating3 = request.form.get('rating3')

    x = int(rating1)
    y = int(rating2)
    z = int(rating3)

    if x + y + z >= 13:
        global picGrade
        picGrade = "Wow! You thought these pics were A+ , glad you liked them so much!"

    elif x + y + z >= 12:
        picGrade = "Glad you liked them! You gave these pics a B"

    elif x + y + z >= 10:
        picGrade = "huh guess these pictures were just ok, you gave them a C"

    elif x + y + z >= 9:
        picGrade = "oh geez not a fan i guess... you gave these pictures an D"

    else:
        picGrade = "you didn't really like these did you... these pictures didn't pass"


    return render_template("rateThis.html")


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

@app.route("/mcq/")
def mcq():
    response = requests.get("https://api.trivia.willfry.co.uk/questions?limit=10")
    output = response.json()
    for x in range(len(output)):
        print(output[x])
    return render_template("mcq.html",questions = output)
if __name__ == "__main__":
    app.run(debug=True, port="5002")
