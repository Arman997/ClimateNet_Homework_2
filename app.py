from flask import Flask, render_template, Response, request, redirect, url_for


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("main.html")

@app.route("/user")
def userPage():
    return render_template("user.html")

@app.route("/final")
def finalPage():
    return render_template("final.html")


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)


