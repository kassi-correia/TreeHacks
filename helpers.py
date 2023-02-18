import os
import requests


from flask import redirect, render_template, request, session
from functools import wraps

# Code for login_required(f) from CS50 finance
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


# Based off of CS50
def apology(message, code=400):
    """Render message as an apology to user."""

    return render_template("apology.html", message=message), code
