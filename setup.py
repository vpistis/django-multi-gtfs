#!/usr/bin/env python
#
# Copyright 2012-2014 John Whitlock
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import unicode_literals

import sys

from setuptools import find_packages, setup
from setuptools.command.test import test

from multigtfs import __version__


class my_test(test):
    def run(self):
        import run_tests
        run_tests.main()


def read(*paths):
    import codecs
    import os.path
    with codecs.open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()


# Handle Py2/Py3 issue
if sys.version_info > (3, 0):
    # In Py3, package data is dict w/ text key
    package_data = {'multigtfs': ['tests/fixtures/*.zip']}
else:
    # In Py2, package data is dict w/ binary string
    package_data = {b'multigtfs': ['tests/fixtures/*.zip']}

setup(
        name='multigtfs',
        version=__version__,
        description='General Transit Feed Specification (GTFS) as a Django app',
        author='John Whitlock',
        author_email='John-Whitlock@ieee.org',
        license='Apache License 2.0',
        url='https://github.com/tulsawebdevs/django-multi-gtfs',
        packages=find_packages(),
        install_requires=['Django>=1.8', 'jsonfield>=0.9.20'],
        keywords='django gtfs',
        test_suite="run_tests",  # Ignored, but makes pyroma happy
        cmdclass={'test': my_test},
        zip_safe=True,
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Framework :: Django",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        include_package_data=True,
        package_data=package_data,
        long_description=read('README.rst')
)
