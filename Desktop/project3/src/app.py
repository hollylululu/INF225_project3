
from flask import Flask, render_template, request

#searchEngine = searchEngine.index("sample")
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("layout.html")

@app.route("/search")
def search():
    query = request.args['q']

    #To do: implete the search part and return s
    #result = searchEngine.search(query)
    #return render_template("result.html", q=query, results=results)