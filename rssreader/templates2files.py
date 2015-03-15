import json
import os 
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment( 
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

ifile = open('../FlaskApp/static/keyword_list.json')
keywords = json.load(ifile)


ofile = open('mod_init.py', 'w')
out_init = TEMPLATE_ENVIRONMENT.get_template('template__init__.tmpl').render(keywords=keywords)

ofile.write(out_init)
ofile.close()

os.system('cp mod_init.py ../FlaskApp/__init__.py')

