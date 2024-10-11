from flask import Flask, request, render_template
from lib import search_def


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    q = request.form["query"]
    defn = search_def(q)
    return render_template("result.html", defn=defn, word=q)

app.run(host="0.0.0.0", port="8000", debug=True)
