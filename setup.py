#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Gustavo Sousa <gustavocms@gmail.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import find_packages, setup

version = '0.1.0'

try:
    long_description = "".join([
        open("README.md").read(),
        open("changelog").read(),
    ])
except:
    long_description = ""

setup(name='TracDynamicOptionsPlugin',
      version=version,
      description="load options for select fields from external sources",
      long_description=long_description,
      author='Gustavo Sousa',
      author_email='gustavocms@gmail.com',
      maintainer='Gustavo Sousa',
      maintainer_email='gustavocms@gmail.com',
      url='http://intranet.hugo-go.net/trac/wiki/DynamicOptionsPlugin',
      keywords='trac plugin',
      license='BSD 3-Clause',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests*']),
      include_package_data=True,
      package_data={'dynamicoptions': []},
      zip_safe=False,
      classifiers=[
          "Framework :: Trac",
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "License :: OSI Approved :: Apache Software License",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development",
      ],
      entry_points="""
      [trac.plugins]
      dynamicoptions.api = dynamicoptions.api
      dynamicoptions.dynamicoptions = dynamicoptions.dynamicoptions
      dynamicoptions.sqlsource = dynamicoptions.sqlsource
      dynamicoptions.jsonsource = dynamicoptions.jsonsource
      """
)

