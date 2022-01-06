# import "packages" from flask
from flask import Flask, render_template,request
import requests
import json
import random
from crud.app_crud import app_crud
from subjects import subjects
import math
# create a Flask instance
from __init__ import app

app.register_blueprint(app_crud)
app.register_blueprint(subjects)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/evan/')
def evan():
    return render_template("about_us/evan.html")

@app.route('/darktest/')
def darktest():
    return render_template("about_us/darktest.html")

@app.route('/leah/')
def leah():
    return render_template("about_us/leah.html")

@app.route('/simon/')
def simon():
    return render_template("about_us/simon.html")

@app.route('/vunsh/')
def vunsh():
    return render_template("about_us/vunsh.html")

@app.route("/sanjay/")
def sanjay():
    options = ["soccer_efl_champ","soccer_epl","soccer_england_efl_cup","soccer_england_league1","soccer_england_league2"]
    selection = options[random.randint(0,len(options)-1)]
    url = "https://odds.p.rapidapi.com/v1/odds"

    querystring = {"sport":"soccer_epl","region":"uk","mkt":"h2h","dateFormat":"iso","oddsFormat":"decimal"}

    headers = {
        'x-rapidapi-host': "odds.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    output =json.loads(response.text)
    url2 = "https://geek-jokes.p.rapidapi.com/api"

    querystring2 = {"format":"json"}

    headers2 = {
        'x-rapidapi-host': "geek-jokes.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }

    response2 = requests.request("GET", url2, headers=headers2, params=querystring2)

    output2 = json.loads(response2.text)
    print(output2)
    return render_template("about_us/sanjay.html",data=output,joke=output2)
@app.route("/final_grade_calc/")
def final_grade_calc():
    return render_template("final_grade_calc.html")
@app.route('/notes/')
def notes():
    return render_template("subjects/notes.html")
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
@app.route('/binary_calc/',methods=['GET', 'POST'])
def binary_calc():
    output = [x+1 for x in range(10)]
    if request.form:
        length = request.form.get("length")
        target = request.form.get('target')
        if len(str(length)) != 0:
            output = sorted(random.sample(range(0,200),int(length)))
        if len(str(target)) == 0:
            target = 2
    print("the target is " + str(target))
    return render_template("compscitools.html",output =output, jsOutput = json.dumps(output), target = target)
@app.route('/courserecoms/')
def courserecoms():
    return render_template('courserecoms.html')


if __name__ == "__main__":
    app.run(debug=True, port="5002")
