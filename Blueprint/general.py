from flask import Blueprint

app = Blueprint("general", __name__)

@app.route("/")
def first_r():
    return "hello world"

@app.route("/about")
def about():
    return "about us"

if __name__ == "__main__":
    app.run(debug=True)