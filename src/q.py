#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Q is a superior life form how can control time and space. It has the hability to
generate data describing planetary position for an specific day in time.

Use example:

.. code-block:: bash

   $ python q.py --days 3
   $ python q.py --years 3
   $ python q.py --years 3 --from-planet Betasoide
"""

import argparse
import json

import matplotlib.pyplot as plt

from forecast import Forecast
from solar import SolarSystem
import config
import database


solar = SolarSystem()
available_planets = ', '.join([p.name for p in solar.planets()])

parser = argparse.ArgumentParser(description='Q data generator.')

parser.add_argument(
    '--from-planet', dest='from_planet', metavar='PLANET', type=str,
    default=solar.vulcano.name,
    help="From which planet's reference will be considered the year "
         "definition. Available names: %s (default: %s)." % (
             available_planets, solar.vulcano.name
         ))

parser.add_argument(
    '--days', dest='days', metavar='N', type=int, default=0,
    help='How many days to calculate.'
)

parser.add_argument(
    '--years', dest='years', metavar='N', type=int, default=0,
    help='How many years to calculate.'
)

parser.add_argument(
    '--plot-all', dest='plot_all', action='store_true', default=False,
    help='Plot all dates to an snapshot with forecast name.'
)

parser.add_argument(
    '--plot-predicted', dest='plot_predicted', action='store_true',
    default=False, help='Plot only predicted weather to an snapshot with '
    'forecast name.'
)

parser.add_argument(
    '--db-clean', dest='db_clean', action='store_true',
    default=False, help='Removes all existent data from database.'
)


def plot(day, name, coords):
    x = [c.delta_to_xy()[0] for c in coords]
    y = [c.delta_to_xy()[1] for c in coords]

    plt.clf()
    plt.axis([-2500, 2500, -2500, 2500])
    fig = plt.gcf()
    ax = fig.gca()
    circle1 = plt.Circle((0, 0), radius=500, color='b', fill=False)
    circle2 = plt.Circle((0, 0), radius=1000, color='b', fill=False)
    circle3 = plt.Circle((0, 0), radius=2000, color='b', fill=False)
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)

    plt.scatter([0], [0])
    plt.plot(x, y)
    plt.title(name)
    plt.savefig('plot/%d-%s.png' % (day, name))


if __name__ == '__main__':
    args = parser.parse_args()

    if args.days == 0 and args.years == 0:
        raise ValueError("An amount of days or years must be indicated.")

    if args.plot_all and args.plot_predicted:
        args.plot_predicted = False

    planet = solar.planet_by_name(args.from_planet)
    if planet is None:
        raise ValueError(
            "You must indicate a planet contained on the solar system. Valid "
            "ones: %s" % available_planets
        )

    db = database.connect()

    if args.db_clean:
        db.flushall()

    total_days = args.days + planet.days_in_year() * args.years
    db.set('total', total_days)
    print("> Total days to calculate: %d (from %s point of view)" % (
        total_days, planet.name
    ))

    fc = Forecast()
    totalized = {'total': total_days, 'max_rain': {'day': None, 'perimeter': 0}}

    for day in range(total_days):
        coords = solar.positions(day)
        prediction = fc.predict(coords)
        totalized.setdefault(prediction['name'], 0)
        totalized[prediction['name']] += 1

        db.set('%s%d' % (config.DB_DAY_PREFIX, day), json.dumps(prediction))

        if prediction['name'] is not None:
            print({
                'day': day,
                'coords': coords,
                'forecast': prediction,
            })

            if args.plot_predicted:
                plot(day, prediction['name'], coords)

        if args.plot_all:
            plot(day, prediction['name'], coords)

        if 'perimeter' in prediction and \
                prediction['perimeter'] > totalized['max_rain']['perimeter']:
            totalized['max_rain']['perimeter'] = prediction['perimeter']
            totalized['max_rain']['day'] = day

    db.set('max_rain', json.dumps(totalized['max_rain']))
    print("Totalization: %s" % totalized)


# vim: ai ts=4 sts=4 et sw=4 ft=python
