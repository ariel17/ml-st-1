#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
United Federation of Planets implementation for Solar System representation.
"""

import math
import numpy


class Position:
    """
    A planet position representation and utilities.

    :param Planet planet: An instance of a planet to represent.
    :param int day: The day number to represent.
    :param float delta: The position displacement for the given day, in radians.
    """

    def __init__(self, planet, day, delta):
        self.planet = planet
        self.day = day
        self.delta = delta  # assuming radians

    def __round(self, value):
        return 0 if numpy.allclose(value, 0) else value

    def delta_to_xy(self):
        """
        Converts current radian position to cartesian coordenates.

        :returns: A `[x, y]` array representing cartesian coordenates.
        :rtype: array
        """
        point = (
            self.planet.distance * self.__round(math.cos(self.delta)),
            self.planet.distance * self.__round(math.sin(self.delta))
        )
        return point

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "<Position planet='%s' day=%d delta=%s>" % (
            self.planet.name, self.day, self.delta
        )


class Planet:
    """
    A planet representation of the solar system for weather forecast.

    :param str name: Planet name to use.
    :param int distance: Distance to Sun in kilometers.
    :param int angular_speed: Angular speed **in deegress**.
    :param bool is_clockwise: Does the planet round in clockwise orientation?
                              Default: `True`.
    """

    def __init__(self, name, distance, angular_speed, is_clockwise=True):
        self.name = name
        self.distance = distance
        self.angular_speed = -angular_speed if is_clockwise else angular_speed

    def days_in_year(self):
        """
        Based on its angular speed, it returns how many days takes to complete
        an orbit.

        :rtype: int
        """
        return abs(int((2 * math.pi) / math.radians(self.angular_speed)))

    def position(self, day):
        """
        Creates a Position object corresponding to the indicated day.

        :rtype: Position
        """
        delta = math.radians(self.angular_speed) * day
        return Position(self, day, delta)


class SolarSystem:
    """
    A solar system representation. It already knows which planets it has.
    """

    def __init__(self):
        self.ferengi = Planet('Ferengi', 500, 1)
        self.betasoide = Planet('Betasoide', 2000, 3)
        self.vulcano = Planet('Vulcano', 1000, 5, False)

    def planets(self):
        """
        Returns a list of planets in the system.

        :rtype: list
        """
        return [self.ferengi, self.betasoide, self.vulcano]

    def planet_by_name(self, name):
        """
        Returns the Planet instance associated to the given name, if it exists.

        :param str name: The planet name to fetch.
        :returns: The Planet name associated, if exists.
        :rtype: Planet
        """
        for planet in self.planets():
            if planet.name == name:
                return planet

        return None

    def positions(self, day):
        """
        Returns a list with all positions for all planets for a given day.

        :param int day: The day number to represent.
        :returns: All planetary position representation.
        :rtype: list
        """
        return [p.position(day) for p in self.planets()]


# vim: ai ts=4 sts=4 et sw=4 ft=python
