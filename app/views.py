#! /usr/bin/python3.6m
# -*- coding:utf-8 -*-
from flask import flash, request, render_template, url_for

from app import app
from .emails import send_email
from .forms import ContactForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        flash('veuillez remplir le formulaire')
        nom = request.form.get('nom')
        email = request.form.get('email')
        message = request.form.get('message')
        send_email(nom, email, message)
        return render_template('index.html', form=form)

    else:
        flash('Le formulaire comporte des erreurs')
        print('wrong')
        return render_template('index.html', form=form)


    return render_template('index.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)