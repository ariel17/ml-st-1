#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO
"""

import json

from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

import config
import database


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('day', type=int, help='Day must be numeric')

db = database.connect()


class Weather(Resource):
    """
    TODO
    """

    def __weather_repr(self, key, day=None):
        """
        TODO
        """
        raw = db.get(key)
        if not raw:
            return None

        weather = json.loads(raw)

        return {
            'day': day if day else int(key.replace(config.DB_DAY_PREFIX, '')),
            'weather': weather['name']
        }

    def get(self):
        """
        TODO
        """
        args = parser.parse_args()

        if args['day']:
            weather_json = self.__weather_repr(
                '%s%d' % (config.DB_DAY_PREFIX, args['day'])
            )

            if not weather_json:
                abort(
                    404,
                    message="Forecast for day %d does not exist" % args['day']
                )

            return weather_json

        keys = db.keys('%s*' % config.DB_DAY_PREFIX)
        if not bool(keys):
            abort(404, message="There is no forecast for any day")

        return {
            'weathers': [self.__weather_repr(k.decode('utf-8')) for k in keys],
            'meta': {
                'total_days': len(keys),
                'max_rain': json.loads(db.get('max_rain')),
            }
        }


api.add_resource(Weather, '/weather')


if __name__ == '__main__':
    app.run(debug=True)
