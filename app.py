from flask import Flask, render_template, url_for, request
import jinja2

from database import EnsembleDatabaseConnector
from customFilter import reg_replace

app = Flask(__name__)
jinja2.filters.FILTERS['reg_replace'] = reg_replace


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/afvinkopdracht1', methods=['POST', 'GET'])
def afvink1():

    if request.method == 'POST':
        zoekterm = request.form['zoekterm']
        edb = EnsembleDatabaseConnector()
        res = edb.searchGenes(zoekterm)
        return render_template("afvink1.html", res=res, zoekt=zoekterm)
    else:
        return render_template("afvink1.html")


if __name__ == '__main__':
    app.run(debug=True)
