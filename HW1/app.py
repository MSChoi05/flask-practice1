from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    hobby = {"Watching youtube", "Playing game", "Reading novel"}
    return render_template("profile.html", hobby = hobby)

if __name__ == "__main__":
    app.run(debug=True)