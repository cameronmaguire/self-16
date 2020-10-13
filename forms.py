from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, SubmitField, validators

class ContactUsForm(Form):
    first_name = TextField("first_name", [validators.Required()])
    last_name = TextField("last_name", [validators.Required()])
    email = TextField("email", [validators.Required(), validators.Email()])
    message = TextAreaField("message", [validators.Required()])
    submit = SubmitField("send")