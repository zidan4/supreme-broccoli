from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/<user>")
def users(user):
  return f"Hello {user}"

@app.route("/<user>/<int:age>")
def user_age(user, age):
  return f"Hello {user}, you are {age} years old."

content = ["Python", "Flask", "Web Development"]

@app.route("/con")
def con():
  return render_template("con.html", content=content)


if __name__ == '__main__':
  app.run(debug=True)

