#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
United Federation of Planets implementation for Solar System representation.
"""

import math
import numpy
from angles import normalize


class Position:

    def __init__(self, planet, day, delta):
        self.planet = planet
        self.day = day
        self.delta = delta  # assuming radians

    def __round(self, value):
        return 0 if numpy.allclose(value, 0) else value

    def delta_to_xy(self):
        """
        TODO
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
    """

    def __init__(self, name, distance, angular_speed, is_clockwise=True):
        self.name = name
        self.distance = distance
        self.angular_speed = -angular_speed if is_clockwise else angular_speed

    def days_in_year(self):
        """
        Based on its angular speed, it returns how many days takes to complete
        an orbit.
        """
        return abs(int((2 * math.pi) / math.radians(self.angular_speed)))

    def position(self, day):
        """
        TODO
        """
        delta = math.radians(self.angular_speed) * day
        return Position(self, day, delta)


class SolarSystem:
    """
    TODO
    """

    def __init__(self):
        self.ferengi = Planet('Ferengi', 500, 1)
        self.betasoide = Planet('Betasoide', 2000, 3)
        self.vulcano = Planet('Vulcano', 1000, 5, False)

    def planets(self):
        """
        TODO
        """
        return [self.ferengi, self.betasoide, self.vulcano]

    def planet_by_name(self, name):
        """
        TODO
        """
        for planet in self.planets():
            if planet.name == name:
                return planet

        return None

    def positions(self, day):
        """
        TODO
        """
        return [p.position(day) for p in self.planets()]


# vim: ai ts=4 sts=4 et sw=4 ft=python
