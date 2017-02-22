#!/usr/bin/env python
'''
utilities to make render/java/web/life interfacing easier
'''
import logging
import json

logger = logging.getLogger(__name__)


def jbool(val):
    '''return string representing java string values of py booleans'''
    if not isinstance(val, bool):
        logger.warning('Evaluating javastring of non-boolean {} {}'.format(
            type(val), val))
    return 'true' if val else 'false'


def stripLogger(logger_tostrip):
    '''
    remove all handlers from a logger -- useful for redefining
    input:
        logger_tostrip: logging logger as from logging.getLogger
    '''
    if logger_tostrip.handlers:
        for handler in logger_tostrip.handlers:
            logger_tostrip.removeHandler(handler)


def _load_dict(obj, d):
    obj.__dict__.update({k: v for k, v in d.items()})


def _load_json(obj, j):
    '''load object from dictionary-style json'''
    with open(j, 'r') as f:
        jd = json.load(f)
    _load_dict(obj, jd)