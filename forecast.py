#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Weather prediction algorithm implementation.
"""

import numpy


OPOSITE_ANGLE_GRADES = 180


class Weather:
    """
    TODO
    """

    def __init__(self, name, coords):
        self.name = name
        self._coords = coords

    def cross_product(self, p1, p2):
        a1 = numpy.array(p1)
        a2 = numpy.array(p2)

        cross = numpy.cross(a1, a2)
        return cross

    def diff(self, p1, p2):
        return numpy.array(p1) - numpy.array(p2)

    def check(self):
        """
        TODO
        """
        raise NotImplementedError('Implement me!')


class Drought(Weather):
    """
    TODO
    """

    def __init__(self, coords):
        super(Drought, self).__init__('drought', coords)

    def check(self):
        """
        Predicts if current coordenates derivates in drought.

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
    TODO
    """
    def __init__(self, coords):
        super(Rain, self).__init__('rain', coords)

    def check(self):
        """
        Verifies if weather condition for rain is given.

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


class Optimal(Weather):
    """
    TODO
    """
    def __init__(self, coords):
        super(Optimal, self).__init__('optimal', coords)

    def check(self):
        """
        Verifies if optimal weather conditions are given.
        """
        [p1, p2, p3] = [c.delta_to_xy() for c in self._coords]

        v1 = self.diff(p1, p2)
        v2 = self.diff(p2, p3)

        cross = self.cross_product(v1, v2)
        return cross == 0


class Forecast:

    def predict(self, coords):
        """
        TODO
        """

        for weather in [Drought(coords), Rain(coords), Optimal(coords)]:
            if weather.check():
                return weather.name

        return None


# vim: ai ts=4 sts=4 et sw=4 ft=python
