import os
import json
from flask import Flask
from flask import Flask, request
from flask import render_template
from flask import g
from flask import jsonify
from flask import redirect

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return render_template('stream.html')

@app.route('/bias', methods = ['POST', 'GET'])
def bias():
    if request.method == 'POST':
        article_url = request.form["article_url"]
        article_info = ""
        #article_info = processURL(article_url)
        return render_template('bias.html', article_info = article_info)
    return render_template('bias.html')



@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        query = request.form["search_query"]
        articles_info=""
        #articles_info = manualSearch(query)
        return render_template('search.html', articles_info = articles_info)
    return render_template('search.html')


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run()
    app.debug = True