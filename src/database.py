#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Database connection module. It hides some *complexity* getting connection
parameters and performing the connection itself.
"""

import os

import redis

import config


def connect():
    """
    Gains environment values or default for database host and port values and
    connects; it returns the client object.

        >>> import database
        >>> db = database.connect()
    """
    db = redis.StrictRedis(
        host=os.environ.get(config.REDIS_HOST_KEY, config.REDIS_HOST_DEFAULT),
        port=os.environ.get(config.REDIS_PORT_KEY, config.REDIS_PORT_DEFAULT),
        db=os.environ.get(
            config.REDIS_CONTEXT_KEY, config.REDIS_CONTEXT_DEFAULT
        )
    )

    return db


# vim: ai ts=4 sts=4 et sw=4 ft=python
