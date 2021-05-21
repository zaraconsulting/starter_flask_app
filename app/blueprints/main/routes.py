from . import bp as main
from flask import render_template, redirect, url_for

@main.route('/')
def index():
    context = dict()
    return render_template('main/index.html', **context)