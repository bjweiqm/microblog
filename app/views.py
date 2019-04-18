#!/usr/bin/env python
# encoding: utf-8

from app import app


@app.route('/')
@app.route('/index/')
def index():

    return 'hello world!'


if __name__ == '__main__':
    app.run()
