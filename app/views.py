from flask import Flask, request, render_template, redirect

@app.errorhandler(404)
def page_not_found(error):
    url = request.referrer 
    short_url = url
    return redirect(short_url)