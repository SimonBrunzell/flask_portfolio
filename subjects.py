from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests

subjects = Blueprint('subjects', __name__)

@subjects.route('/apec/')
def apec():
    return render_template("subjects/apec.html")

@subjects.route('/apush/')
def apush():
    return render_template("subjects/apush.html")

@subjects.route('/biology/')
def biology():
    return render_template("subjects/biology.html")

@subjects.route('/calcab/')
def calcab():
    return render_template("subjects/calcab.html")

@subjects.route('/chemistry/')
def chemisty():
    return render_template("subjects/chemistry.html")

@subjects.route('/csp/')
def csp():
    return render_template("subjects/csp.html")

@subjects.route('/stats/')
def stats():
    return render_template("subjects/stats.html")

@subjects.route('/notes/')
def notes():
    return render_template("subjects/notes.html")

