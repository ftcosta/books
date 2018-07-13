import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=["GET", "POST"])
def index():

    if session.get("user_id") is None:
        session["user_id"] = ""

    if request.method == "POST":
        submit = None
        if request.form.get("sign-in"): submit = "sign-in"
        if request.form.get("sign-up"): submit = "sign-up"

        if submit is not None:
            return render_template("index.html", register=False, post=True, submit=submit)
        else:
            register = request.args.get('sign') == 'up'
            return render_template("index.html", register=register, post=False)
    else:
        register = request.args.get('sign') == 'up'
        return render_template("index.html", register=register, post=False)









#
