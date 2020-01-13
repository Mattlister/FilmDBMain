from flask import Flask, render_template

app = Flask (__name__)

@app.route("/index")
def index ():
    return render_template("index.html")

@app.route("/films")
def films ():
    return render_template("films.html")    

@app.route("/tv")
def tv():
    return render_template("tv.html")

@app.route("/casting")
def casting():
    return render_template("casting.html")

@app.route("/discover")
def discover():
    return render_template("discover.html")

@app.route("/filmdata")
def filmdata():
    return render_template("filmdata.html")  

@app.route("/login")
def filmdata():
    return render_template("login.html")  

@app.route("/signup")
def filmdata():
    return render_template("signup.html")  


if __name__ == "__main__":
    app.run(debug=True)
