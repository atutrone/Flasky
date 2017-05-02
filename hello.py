from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField ('What is your name?', validators=[Required()])
    #"Required" sets the string field to be needed in order for the form to submit successfully.  Will return error that the field is empty.
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsNotSecure'
bootstap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None                                     #'name' will hold the name submitted once button is pressed.  For now, 'None' is used
    form = NameForm()                               #Instance of our NameForm class created
    if form.validate_on_submit():                   #Will return true when formed is submitted and data clears validation.  For this to return true, the field must be populated with a name
        name = form.name.data                       #takes the value submitted by the user and sets 'name' variable to it.  'form.name.data' pulls the value from the html text field.
        form.name.data = ''
    return render_template('index.html', form=form, name=name, current_time=datetime.utcnow())
    #When the page is first accessed, the form has no data so render_template is invoked, because the if statement above results to 'false'(i.e., no info submitted)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)