from flask import Flask, render_template, request
from forms import ContactUsForm
from flask_mail import Message, Mail
from secrets import SECRET_KEY, MAIL_USERNAME, MAIL_PASSWORD, RECIPIENTS

mail = Mail()

app = Flask(__name__)

app.secret_key = SECRET_KEY

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = MAIL_USERNAME
app.config["MAIL_PASSWORD"] = MAIL_PASSWORD

mail.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/requirements')
def requirements():
    return render_template('requirements.html')

@app.route('/connectivity')
def connectivity():
    return render_template('connectivity.html')

@app.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    form = ContactUsForm()

    if request.method == 'POST':
        if form.validate() == True:
            msg = Message('New Message SELF-16',
                          sender=('SELF-16 DoNotReply', MAIL_USERNAME),
                          recipients = RECIPIENTS)
            msg.body = """Name:
%s %s

Email:
%s <mailto:%s>

Message:
%s

________________________________

This message was submitted from your website contact form""" % (form.first_name.data, form.last_name.data, form.email.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('contact-us.html', success=True)
        else:
            render_template('contact-us.html', form=form)

    elif request.method == 'GET':
        return render_template('contact-us.html', form=form)

@app.route('/sea-trials')
def sea_trials():
    return render_template('sea-trials.html')

if __name__ == '__main__':
    app.run()
