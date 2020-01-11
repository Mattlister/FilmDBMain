from flask import Flask, redirect, url_for

app = Flask (__name__)

@app.route("/")
def home ():
    return "Welcome to FilmDB!"

@app.route("/Films")
def Films():
    return "Films"

@app.route("/TV")
def TV():
    return "TV"

@app.route("/Casting")
def Casting():
    return "Casting"
    
if __name__ == "__main__":
    app.run(debug=True)
