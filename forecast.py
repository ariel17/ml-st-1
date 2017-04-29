#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Weather prediction algorithm implementation.
"""

from angles import normalize


OPOSITE_ANGLE_GRADES = 180


class Weather:
    """
    TODO
    """

    def __init__(self, coords):
        self._coords = coords

    def predict(self):
        """
        TODO
        """
        raise NotImplementedError('Implement me!')


class Drought(Weather):
    """
    TODO
    """

    def predict(self):
        """
        Predicts if current coordenates derivates in drought.

        >>> Drought({'A': 90, 'B': 90, 'C': 90}).predict()
        True
        >>> Drought({'A': 0, 'B': 0, 'C': 180}).predict()
        True
        >>> Drought({'A': 180, 'B': 0, 'C': 180}).predict()
        True
        """
        return any([self._same_angle(), self._oposite_angle()])

    def _same_angle(self):
        """
        Verifies if all angles are equals.

        >>> Drought({'A': 90, 'B': 90, 'C': 90})._same_angle()
        True
        >>> Drought({'A': 90, 'B': 90, 'C': 89})._same_angle()
        False
        """
        [p1, p2, p3] = self._coords.values()
        return p1 == p2 == p3

    def _oposite_angle(self):
        """
        Verifies if angles are oposite and/or some are equals.

        >>> Drought({'A': 0, 'B': 0, 'C': 180})._oposite_angle()
        True
        >>> Drought({'A': 180, 'B': 0, 'C': 180})._oposite_angle()
        True
        >>> Drought({'A': 180, 'B': 10, 'C': 180})._oposite_angle()
        False
        """
        [p1, p2, p3] = self._coords.values()
        oposite = normalize(p1 + OPOSITE_ANGLE_GRADES)
        return oposite == p2 == p3 or \
            p1 in [p2, p3] and oposite in [p2, p3]


class Rain(Weather):

    def predict(self):
        """
        TODO
        """
        pass


class Optimal(Weather):

    def predict(self):
        """
        TODO
        """
        pass





# vim: ai ts=4 sts=4 et sw=4 ft=python
