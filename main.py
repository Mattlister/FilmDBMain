from flask import Flask, render_template

app = Flask (__name__)

@app.route("/index")
def index ():
    return render_template("index.html")


@app.route("/TV")
def TV():
    return "TV"

@app.route("/Casting")
def Casting():
    return "Casting"
   
if __name__ == "__main__":
    app.run(debug=True)
