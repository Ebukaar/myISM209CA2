from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MyISM209CA2db@localhost/MyISM209CA2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from main import db

import models


@app.route("/")
def home():
    return render_template('home.html',
                           title="Chukwuebuka Adigwe. This is my CA2 work. My Github URL is https://github.com/Ebukaar")


@app.route("/products-and-services/")
def products_and_services():
    return render_template('products-and-services.html', title="Products and Services")


@app.route("/about-us/")
def about_us():
    return render_template('about-us.html', title="About Us")


@app.route("/signup/")
def signup():
    return render_template('signup.html', title="SIGN UP", information="Use the form displayed to register")


#@app.route("/process-signup/", methods=['POST'])
def process_signup():
    # Let's get the request object and extract the parameters sent into local variables.
    firstname = request.form['firstname']
    Surname = request.form['Surname']
    othernames = request.form['othernames']
    email = request.form['email']
    password = request.form['password']
    # let's write to the database
    try:
        user = models.User(firstname=firstname, Surname=Surname, othernames=othernames, email=email,
                           password=password)
        db.session.add(user)
        db.session.commit()

    except Exception as e:
        # Error caught, prepare error information for return
        information = 'Could not submit. The error message is {}'.format(e.__cause__)
        return render_template('signup.html', title="SIGN-UP", information=information)

    # If we have gotten to this point, it means that database write has been successful. Let us compose success info

    # Let us prepare success feedback information

    information = 'User by name {} {} successfully added. The login name is the email address {}.'.format(firstname, Surname, email)

    return render_template('signup.html', title="SIGN-UP", information=information)


if __name__ == "__main__":
    app.run(port=5005)
