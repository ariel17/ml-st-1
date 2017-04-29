#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from planets import SolarSystem

"""
Description: Q is a superior life form how can control time and space. It has
the hability to generate data describing planetary position for an specific day
in time.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


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


if __name__ == '__main__':
    args = parser.parse_args()

    if args.days == 0 and args.years == 0:
        raise ValueError("An amount of days or years must be indicated.")

    planet = solar.planet_by_name(args.from_planet)
    if planet is None:
        raise ValueError(
            "You must indicate a planet contained on the solar system. Valid "
            "ones: %s" % available_planets
        )

    total_days = args.days + planet.days_in_year() * args.years
    print("> Total days to calculate: %d (from %s point of view)" % (
        total_days, planet.name
    ))

    for day in range(1, total_days + 1):
        print({
            'day': day,
            'coords': solar.position_coords(day)
        })


# vim: ai ts=4 sts=4 et sw=4 ft=python
