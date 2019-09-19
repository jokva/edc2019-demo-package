#!/usr/bin/env python3

import setuptools

def read(filename):
    with open(filename) as f:
        return f.read()

long_description = read('README.md')

setuptools.setup(
    name = 'my-package',
    author = 'mechazawa',
    author_email = 'mech@equinor.com',
    description = 'my brilliant package',
    long_description = long_description,

    packages = [
        'my_package',
        'my_package.sub',
    ],

    install_requires = [
        'numpy',
    ],

    use_scm_version = True,

    entry_points = {
        'console_scripts': [
            'juan = my_package.__main__:main',
        ],
    },
)
