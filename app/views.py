import sys
sys.path.append(".")
from bot.shortener import return_url
from flask import Flask, request, render_template, redirect


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    url = request.referrer 
    return redirect(return_url(url))
