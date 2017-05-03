#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Shared configuration between modules and applications.
"""

#: Environment variable name for Redis host location.
REDIS_HOST_KEY = 'REDIS_HOST'
#: Default value for Redis host location.
REDIS_HOST_DEFAULT = 'localhost'

#: Environment variable name for Redis port value.
REDIS_PORT_KEY = 'REDIS_PORT'
#: Default value for Redis port value.
REDIS_PORT_DEFAULT = 6379

#: Environment variable name for Redis database id.
REDIS_CONTEXT_KEY = 'REDIS_CONTEXT_KEY'
#: Default value for Redis database id.
REDIS_CONTEXT_DEFAULT = 0

#: Optimal weather error round accepted for consider the sceneario as it.
OPTIMAL_ACEPTABLE_ROUND_ERROR = 0.0002

#: Database key prefix for day prediction entries.
DB_DAY_PREFIX = 'day-'
