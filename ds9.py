#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO
"""

import json

from flask import Flask
from flask_restful import Resource, Api, reqparse

import database


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('day', type=int, help='Day must be numeric')

db = database.connect()


class Weather(Resource):

    def get(self):
        args = parser.parse_args()
        weather = json.loads(db.get(args['day']))
        return {
            'day': args['day'],
            'weather': weather['name']
        }


api.add_resource(Weather, '/weather')


if __name__ == '__main__':
    app.run(debug=True)
