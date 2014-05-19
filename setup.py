#!/usr/bin/env python

from distutils.core import setup

setup(name          = 'gs-pypi',
      version       = '0.1',
      description   = 'g-sorcery backend for pypi packages',
      author        = 'Jauhien Piatlicki',
      author_email  = 'jauhien@gentoo.org',
      packages      = ['gs_pypi'],
      package_data  = {'gs_pypi': ['data/*']},
      scripts       = ['bin/gs-pypi-generate-db', 'bin/gs-pypi'],
      data_files    = [('/etc/g-sorcery/', ['gs-pypi.json']),
                       ('/etc/layman/overlays/', ['gs-pypi-overlays.xml'])],
      license       = 'GPL',
      )
