#!/usr/bin/env python
# -*- coding: utf-8 -*-

from angles import normalize

"""
Description: United Federation of Planets implementation for weather forecast.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


TOTAL_ORBITAL_GRADES = 360


class Planet:
    """
    A planet representation of the solar system for weather forecast.
    """

    def __init__(self, name, distance, angular_speed, is_clockwise=True):
        self.name = name
        self.distance = distance
        self.angular_speed = angular_speed
        self.is_clockwise = is_clockwise

    def days_in_year(self):
        """
        Based on its angular speed, it returns how many days takes to complete
        an orbit.
        """
        return int(TOTAL_ORBITAL_GRADES / self.angular_speed)

    def position_coord(self, day):
        delta = int(normalize(self.angular_speed * day))

        if self.is_clockwise:
            return delta

        return TOTAL_ORBITAL_GRADES - delta


class SolarSystem:

    def __init__(self):
        self.ferengi = Planet('Ferengi', 500, 1)
        self.betasoide = Planet('Betasoide', 2000, 3)
        self.vulcano = Planet('Vulcano', 1000, 5, False)

    def planets(self):
        return [self.ferengi, self.betasoide, self.vulcano]

    def planet_by_name(self, name):
        for planet in self.planets():
            if planet.name == name:
                return planet

        return None

    def position_coords(self, day):
        coords = {}

        for planet in self.planets():
            coords[planet.name] = planet.position_coord(day)

        return coords
