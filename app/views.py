#!/usr/bin/env python
# encoding: utf-8
from flask import render_template()
from app import app


@app.route('/')
@app.route('/index/')
def index():

    user = { 'nickname': 'Miguel' } # fake user
    return 'hello world!'


if __name__ == '__main__':
    app.run()
