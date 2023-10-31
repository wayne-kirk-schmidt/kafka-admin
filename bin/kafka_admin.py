#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pylint: disable=no-name-in-module

"""
Explanation:

    This script is a wrapper for a kafka maintenance

Usage:
    $ python  kafka_admin [ options ]

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

    @name           kafka_admin
    @version        1.0.0
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@changeis.co.jp
    @license-name   Apache
    @license-url    https://www.apache.org/licenses/LICENSE-2.0
"""

__version__ = '1.0.0'
__author__ = "Wayne Schmidt (wayne.kirk.schmidt@changeis.co.jp)"

import sys
import json
import datetime
import argparse
import kafka
### from kafka import KafkaConsumer
