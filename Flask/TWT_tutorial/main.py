from flask import Flask, render_template
from flask import redirect, url_for
from flask import request, session
from flask import flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "SamuelRocks"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


class Users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Para eliminar datos de una base de datos
# Users.query.filter_by(name=user).first()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/view')
def view():
    return render_template("view.html", values=Users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = Users.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = Users(name=user, email="")
            db.session.add(usr)
            db.session.commit()

        flash("Login Succesful!")
        return redirect(url_for("user"))

    elif "user" in session:
        flash("Already logged in!")
        return redirect(url_for("user"))
    
    return render_template("login.html")

@app.route("/user", methods=['POST', 'GET'])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            found_user = Users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")
        else:
            if 'email' in session:
                email = session['email']

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    flash("You have been logged out.", category="info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)