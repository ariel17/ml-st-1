#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DS9 states for Deep Space 9, a Federation station orbiting Bajor. In this
project it works as the API implementation for weather web service requested by
Vulcano.
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
    It is the API resource providing weather information.
    """

    def __weather_repr(self, key, day=None):
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
        GET verb implementation. It receives a non-mandatory parameter called
        `day`, as follows:

        * `/weather`: Retrieves all existent predicted weather in database,
          with some metadata as total days analyzed and peak rain day.
        * `/weather?day=N`: Returns the forecast predicted for the indicated
          day, if it exists on database.
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
    app.run(host='0.0.0.0', debug=True)
