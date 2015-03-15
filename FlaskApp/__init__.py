
from flask import Flask
from flask import render_template, flash, json, request, redirect, url_for
import os
from find_terms import find_terms

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

ifile = open(os.path.join(APP_ROOT,'static','keyword_list.json'))
keywords = json.load(ifile)

for i, kwd in enumerate(keywords):
    if kwd['keyword'].startswith('\"'):
        keywords[i]['keyword'] = kwd['keyword'][1:-1]


@app.route('/')
@app.route('/index')
@app.route('/sea_ice')
def sea_ice():
    
    ifile =open(os.path.join(APP_ROOT,'static', 'sea_ice.json'))
    posts = json.load(ifile)
    ifile.close()
    pname = 'sea_ice'
    return render_template('index.html',
                           title="sea_ice",
                           posts=posts,
                           pname=pname,
                           keywords=keywords)


@app.route('/arctic_ocean')
def arctic_ocean():
    
    ifile =open(os.path.join(APP_ROOT,'static', 'arctic_ocean.json'))
    posts = json.load(ifile)
    ifile.close()
    pname = 'arctic_ocean'
    return render_template('index.html',
                           title="arctic_ocean",
                           posts=posts,
                           pname=pname,
                           keywords=keywords)


@app.route('/glacier')
def glacier():
    
    ifile =open(os.path.join(APP_ROOT,'static', 'glacier.json'))
    posts = json.load(ifile)
    ifile.close()
    pname = 'glacier'
    return render_template('index.html',
                           title="glacier",
                           posts=posts,
                           pname=pname,
                           keywords=keywords)


@app.route('/sea_level')
def sea_level():
    
    ifile =open(os.path.join(APP_ROOT,'static', 'sea_level.json'))
    posts = json.load(ifile)
    ifile.close()
    pname = 'sea_level'
    return render_template('index.html',
                           title="sea_level",
                           posts=posts,
                           pname=pname,
                           keywords=keywords)


@app.route('/ocean_color')
def ocean_color():
    
    ifile =open(os.path.join(APP_ROOT,'static', 'ocean_color.json'))
    posts = json.load(ifile)
    ifile.close()
    pname = 'ocean_color'
    return render_template('index.html',
                           title="ocean_color",
                           posts=posts,
                           pname=pname,
                           keywords=keywords)


@app.route('/journals')
def journals():

    ifile =open(os.path.join(APP_ROOT,'static','journal_list.json'))
    journals = json.load(ifile)
    ifile.close()
    pname = 'journals'

    return render_template('journals.html',
                           title='List of journals',
                           journals=journals,
                           pname=pname,
                           keywords=keywords)
    
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        rres = request.form['searchphrase']
        posts = find_terms(rres)
        return render_template('search_results.html', 
                                rres=rres,
                                posts=posts,
                                request=rres,
                                keywords=keywords)
    pname = 'search'
    return render_template('search.html',
                           title='Search',
                           journals=journals,
                           pname=pname,
                           keywords=keywords)

if __name__ == "__main__":
    app.run()