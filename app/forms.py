from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired("Tapez votre Nom")])
    email = StringField('Email', validators=[DataRequired("Tapez votre email"), Email()])
    message = TextAreaField('Message', validators=[DataRequired("Tapez votre message")])
    submit = SubmitField('Envoyez')