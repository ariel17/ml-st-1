#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO
"""

import os

import redis

import config


def connect():
    """
    TODO
    """
    db = redis.StrictRedis(
        host=os.environ.get(config.REDIS_HOST_KEY, config.REDIS_HOST_DEFAULT),
        port=os.environ.get(config.REDIS_PORT_KEY, config.REDIS_PORT_DEFAULT),
        db=os.environ.get(
            config.REDIS_CONTEXT_KEY, config.REDIS_CONTEXT_DEFAULT
        )
    )

    print("Connected :)")
    return db


# vim: ai ts=4 sts=4 et sw=4 ft=python
