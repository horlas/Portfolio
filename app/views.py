#! /usr/bin/python3.6m
# -*- coding:utf-8 -*-
from flask import Flask, flash, request, render_template, url_for
from app import app
from  .forms import ContactForm



@app.route('/')
def index():
    form = ContactForm()
    # if request.method == 'POST':
    #     if form.validate() == False:
    #         flash('You must enter something into all of the fields')
    #         return render_template('index.html', form=form)
    #     else:
    #        # msg = Message(form.subject.data, sender='[SENDER EMAIL]', recipients=['[RECIPIENT EMAIL]'])
    #         # msg.body = """
    # 		#	From: %s %s <%s>
    # 		#	%s
    # 			""" % (form.firstName.data, form.lastName.data, form.email.data, form.message.data)
    #         mail.send(msg)
    #         return render_template('contact.html', success=True)
    # elif request.method == 'GET':
    #     return render_template('contact.html',
    #                            title='Contact Us',
    #                            form=form)

    return render_template('index.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)