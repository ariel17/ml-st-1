#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Weather prediction algorithm implementation.
"""

import numpy

import config


class Weather:
    """
    Base implementation for weather algorithms.

    :param str name: The weather name to represent.
    :param list coords: A list containing `solar.Position` objects for each
                        planet.
    """

    def __init__(self, name, coords):
        self.name = name
        self._coords = coords

    def cross_product(self, p1, p2):
        """
        Cross product for points `p1` and `p2` (vector from origin
        representations).

        :param array p1: An array representation of cartesian coords `[x, y]`
                         for the first point.
        :param array p2: An array representation of cartesian coords `[x, y]`
                         for the second point.
        :returns: It represents the area of formed parallelogram between the
                  vectors.
        :rtype: float
        """
        a1 = numpy.array(p1)
        a2 = numpy.array(p2)

        cross = numpy.cross(a1, a2)
        return cross

    def diff(self, p1, p2):
        """
        Difference vector for 2 points (vector from origin representations)

        :param array p1: An array representation of cartesian coords `[x, y]`
                         for the first point.
        :param array p2: An array representation of cartesian coords `[x, y]`
                         for the second point.
        :returns: A new vector as the difference between the vectors to given
                  points.
        :rtype: numpy.array
        """
        return numpy.array(p1) - numpy.array(p2)

    def check(self):
        """
        Applies weather algorithm to given data to validate it, but just an
        skeleton for heritage.
        """
        raise NotImplementedError('Implement me!')

    def is_rain(self):
        """
        Indicates if current implementation corresponds to Rain weather or not.

        :rtype: bool
        """
        return False


class Drought(Weather):
    """
    Drought algorithm implementation.

    :param list coords: A list containing `solar.Position` objects for each
                        planet.
    """

    def __init__(self, coords):
        super(Drought, self).__init__('drought', coords)

    def check(self):
        """
        Predicts if current coordenates derivates in drought.

        :returns: `True` when all planets all aligned between and the Sun.
        :rtype: bool

        >>> from math import radians, pi
        >>> from solar import SolarSystem, Position
        >>> ss = SolarSystem()
        >>> Drought([
        ...     Position(ss.vulcano, 1, radians(90)),
        ...     Position(ss.betasoide, 1, radians(90)),
        ...     Position(ss.ferengi, 1, radians(90))
        ... ]).check()
        True
        >>> Drought([
        ...     Position(ss.vulcano, 1, radians(0)),
        ...     Position(ss.betasoide, 1, radians(0)),
        ...     Position(ss.ferengi, 1, radians(180))
        ... ]).check()
        True
        >>> Drought([
        ...     Position(ss.vulcano, 1, radians(180)),
        ...     Position(ss.betasoide, 1, radians(0)),
        ...     Position(ss.ferengi, 1, radians(180))
        ... ]).check()
        True
        """
        [p1, p2, p3] = [c.delta_to_xy() for c in self._coords]
        return self.cross_product(p1, p2) == 0 and \
            self.cross_product(p1, p3) == 0 and self.cross_product(p1, p3) == 0


class Rain(Weather):
    """
    Rain algorithm implementation.

    :param list coords: A list containing `solar.Position` objects for each
                        planet.
    """
    def __init__(self, coords):
        super(Rain, self).__init__('rain', coords)

    def is_rain(self):
        return True

    def check(self):
        """
        Verifies if weather condition for rain is given. The Sun must be inside
        the triangle formed by all unaligned planets.

        Sources:

        * |1|_
        * |2|_
        * |3|_

        .. |1| replace:: Number of Triangles Containing The Point (0,0)
        .. _1: http://stackoverflow.com/questions/27713046/number-of-triangles-containing-the-point-0-0

        .. |2| replace:: How to determine if a point is in a 2D triangle?
        .. _2: http://stackoverflow.com/questions/2049582/how-to-determine-if-a-point-is-in-a-2d-triangle

        .. |3| replace:: PerroAzul's jsfiddle
        .. _3: http://jsfiddle.net/PerroAZUL/zdaY8/1/

        >>> from math import radians
        >>> from solar import SolarSystem, Position
        >>> ss = SolarSystem()
        >>> Rain([
        ...     Position(ss.vulcano, 1, radians(20)),
        ...     Position(ss.betasoide, 1, radians(175)),
        ...     Position(ss.ferengi, 1, radians(240))
        ... ]).check()
        True
        >>> Rain([
        ...     Position(ss.vulcano, 1, radians(15)),
        ...     Position(ss.betasoide, 1, radians(90)),
        ...     Position(ss.ferengi, 1, radians(120))
        ... ]).check()
        False
        """
        [p1, p2, p3] = [c.delta_to_xy() for c in self._coords]

        dx = 0 - p3[0]
        dy = 0 - p3[1]

        dx21 = p3[0] - p2[0]
        dy12 = p2[1] - p3[1]

        dd = dy12 * (p1[0] - p3[0]) + dx21 * (p1[1] - p3[1])
        s = dy12 * dx + dx21 * dy
        t = (p3[1] - p1[1]) * dx + (p1[0] - p3[0]) * dy

        if dd < 0:
            return s <= 0 and t <= 0 and s+t >= dd

        return s >= 0 and t >= 0 and s+t <= dd

    def perimeter(self):
        """
        Determines the perimeter of the formed triangle by all planets.

        :returns: The perimeter value.
        :rtype: float
        """
        [p1, p2, p3] = [c.delta_to_xy() for c in self._coords]

        v1 = self.diff(p1, p2)
        v2 = self.diff(p2, p3)
        v3 = self.diff(p1, p3)

        v1_norm = numpy.linalg.norm(v1)
        v2_norm = numpy.linalg.norm(v2)
        v3_norm = numpy.linalg.norm(v3)

        return v1_norm + v2_norm + v3_norm


class Optimal(Weather):
    """
    Optimal weather algorithm implementation.

    :param list coords: A list containing `solar.Position` objects for each
                        planet.
    """
    def __init__(self, coords):
        super(Optimal, self).__init__('optimal', coords)

    def check(self):
        """
        Verifies if optimal weather conditions are given.

        :returns: `True` when all planets are aligned but the Sun.
        :rtype: bool
        """
        [p1, p2, p3] = [c.delta_to_xy() for c in self._coords]

        v1 = self.diff(p1, p2)
        v2 = self.diff(p2, p3)

        cross = self.cross_product(v1, v2)
        dot = numpy.dot(v1, v2)
        v1_norm = numpy.linalg.norm(v1)
        v2_norm = numpy.linalg.norm(v2)

        cos = abs(dot / (v1_norm * v2_norm))

        return cross == 0 or \
            1 > cos >= (1 - config.OPTIMAL_ACEPTABLE_ROUND_ERROR)


class Forecast:
    """
    A factory class for all weather implementations that applies to every day
    in order to predict future conditions.
    """

    def predict(self, coords):
        """
        Applies all algorithms to a given date to find which one matches, if
        any.

        :param list coords: A list containing lists of `solar.Position` objects
                            for each planet, for each day.
        :returns: A dictionary containing the predicted weather name and, if
                  it is corresponds, the triangle perimeter.
        :rtype: dict
        """

        for weather in [Drought(coords), Rain(coords), Optimal(coords)]:
            result = {'name': None}
            if weather.check():
                result['name'] = weather.name
                if weather.is_rain():
                    result['perimeter'] = weather.perimeter()
                return result

        return {'name': None}


# vim: ai ts=4 sts=4 et sw=4 ft=python
