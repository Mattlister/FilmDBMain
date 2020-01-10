from flask import Flask

app = Flask (__name__)

@app.route("/")
def home ():
    return "Welcome to FilmDB!"

@app.route("/Films")
def Films():
    return "Films"


if __name__ == "__main__":
    app.run(debug=True)
