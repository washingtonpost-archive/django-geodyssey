#!/usr/bin/env python
from distutils.core import setup

setup(name='django-geodyssey',
        version='0.1',
        description='A Django application for storing geographies and related events.',
        author='Jeremy Bowers',
        author_email='bowersj@washpost.com',
        url='https://github.com/wpmedia/django-geodyssey',
        packages = ['geodyssey',],
        license = 'MIT',
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Utilities'
        ],
)
