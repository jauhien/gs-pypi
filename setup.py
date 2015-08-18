#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    setup.py
    ~~~~~~~~

    installation script

    :copyright: (c) 2013-2015 by Jauhien Piatlicki
    :license: GPL-2, see LICENSE for more details.
"""

from distutils.core import setup

setup(name          = 'gs-pypi',
      version       = '0.2.1',
      description   = 'g-sorcery backend for pypi packages',
      author        = 'Jauhien Piatlicki',
      author_email  = 'jauhien@gentoo.org',
      packages      = ['gs_pypi'],
      package_data  = {'gs_pypi': ['data/*']},
      scripts       = ['bin/gs-pypi-generate-db', 'bin/gs-pypi'],
      data_files    = [('/etc/g-sorcery/', ['gs-pypi.json']),
                       ('/etc/layman/overlays/', ['gs-pypi-overlays.xml'])],
      license       = 'GPL-2',
      )
