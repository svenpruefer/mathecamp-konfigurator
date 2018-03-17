#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(svenpruefer): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='mathecamp_konfigurator',
    version='0.1.0',
    description="Mathecamp-konfigurator allows you to plan and organize your own Mathecamp.",
    long_description=readme + '\n\n' + history,
    author="Sven Pruefer",
    author_email='pruefer.sven@gmail.com',
    url='https://github.com/svenpruefer/mathecamp_konfigurator',
    packages=find_packages(include=['mathecamp_konfigurator']),
    entry_points={
        'console_scripts': [
            'mathecamp_konfigurator=mathecamp_konfigurator.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='mathecamp_konfigurator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
