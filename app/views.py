from flask import render_template, flash, redirect, session, url_for
from flask import request, g, abort, jsonify, send_file, json
from werkzeug import secure_filename, FileStorage
from app import app

def build_block(keyword, icon=''):
	titlecase = keyword[0].upper() + keyword[1:]
	block = """<a href="/?keyword=%s"><div class="green %s">%s</div></a>""" % (keyword, icon, titlecase)
	return block
app.jinja_env.globals.update(build_block=build_block)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')