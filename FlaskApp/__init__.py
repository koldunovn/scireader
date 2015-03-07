from flask import Flask
from flask import render_template, flash, json


app = Flask(__name__)

import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

@app.route('/')
@app.route('/index')
def index():
    
    ifile =open(os.path.join(APP_ROOT,'sea_ice.json'))
    posts = json.load(ifile)
    ifile.close()
    pname = 'sea_ice'
    return render_template('index.html',
                           title='Sea ice',
                           user='Nikolay',
                           posts=posts,
                           pname=pname)

@app.route('/arctic_ocean')
def arctic_ocean():

    ifile =open(os.path.join(APP_ROOT,'arctic_ocean.json'))
    posts = json.load(ifile)
    ifile.close()
    pname = 'arctic_ocean'

    return render_template('index.html',
                           title='Arctic Ocean',
                           user='Nikolay',
                           posts=posts,
                           pname=pname)

@app.route('/glacier')
def glacier():

    ifile =open(os.path.join(APP_ROOT,'glacier.json'))
    posts = json.load(ifile)
    ifile.close()
    pname = 'glacier'

    return render_template('index.html',
                           title='Glacier',
                           user='Nikolay',
                           posts=posts,
                           pname=pname)

@app.route('/climate_sensitivity')
def climate_sensitivity():

    ifile =open(os.path.join(APP_ROOT,'climate_sensitivity.json'))
    posts = json.load(ifile)
    ifile.close()
    pname = 'climate_sensitivity'

    return render_template('index.html',
                           title='Climate Sensitivity',
                           user='Nikolay',
                           posts=posts,
                           pname=pname)



#@app.route('/')
#def homepage():
#    return "Hi there, how ya doin?"


if __name__ == "__main__":
    app.run(debug=True)

