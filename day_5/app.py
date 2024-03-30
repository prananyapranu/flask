from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/thankyou", methods=['POST'])
def registration():
    uname = request.form.get("user_name")
    uage = int(request.form.get("user_age"))
    return render_template("thankyou.html", uname=uname, uage=uage)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
