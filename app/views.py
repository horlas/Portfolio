#! /usr/bin/python3.6m
# -*- coding:utf-8 -*-
from flask import flash, request, render_template, url_for

from app import app
from .emails import send_email
from .forms import ContactForm

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404



@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    if request.method == 'POST' and form.validate():
        nom = request.form.get('nom')
        email = request.form.get('email')
        message = request.form.get('message')
        send_email(nom, email, message)
        flash('merci pour votre message')
        # return empty message
        message = form.message.data
        form.message.data = ''
        return render_template('index.html', form=form, message=message)
    else:
        flash('le formulaire comporte des erreurs')
        return render_template('index.html', form=ContactForm())




if __name__ == '__main__':
    app.run(debug=True)